from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from users.models import User
from chatmessages.models import ChatMessage
from friends.models import Friends
from notification.models import Notifications


class ChatConsumer(WebsocketConsumer):
    """
    This is the consumer class for django channels.
    """
    msg_id = 0

    def save_message(self, username, room, message):
        """
        This view saves the message sent over websocket in database.

        :param username: username of sender.
        :param room: room used for chatting.
        :param message: Message that is being sent.
        :return: True if message is saved, False if some error has occurred.
        """
        try:
            user_obj = User.objects.get(username=username)
        except Exception as e:
            print(e.__str__())
            return True

        friend_obj = Friends.objects.filter(user1=user_obj, room_name=room)

        if friend_obj:
            # check if sender is user1 in Friends model.
            try:
                chat_message = ChatMessage.objects.create(sender=user_obj, receiver=friend_obj[0].user2,
                                                          message=message)
                chat_message.save()
                self.msg_id = chat_message.pk

            except Exception as e:
                print(e.__str__())
                return False
            else:
                return True
        else:
            # if sender is not user1 then get friend by filtering with user2.
            try:
                friend_obj = Friends.objects.get(user2=user_obj, room_name=room)
                chat_message = ChatMessage.objects.create(sender=user_obj, receiver=friend_obj.user1, message=message)

                chat_message.save()
                self.msg_id = chat_message.pk

            except Exception as e:
                print(e.__str__())
                return True
            else:
                return True

    def get_friend_username(self, my_username, room_name):
        """
        This view return friend username based on notification room_name.
        If room is for chat purpose then it will returns none, else room is used for sent notification then it will return
        username of user.

        :param room_name: room for chat or sent notification
        :return: friend username or none based on condition
        """

        friend_obj = Notifications.objects.filter(room=room_name)
        if friend_obj:
            friend_username = friend_obj[0].user.username
            return friend_username
        return None

    def connect(self):
        """
        This view is use for join room group.
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """
        This view is used for leave from room group
        """
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        """
        This view is receive message from websocket & send it into room group.

        :param text_data: text_data(data-type: JSON) is used for get which message being sent and to whom to send.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        notification = text_data_json['notification']
        # Send message to room group
        if not message.strip() == "":

            message_response = self.save_message(username, self.room_name, message)
            friend_username = self.get_friend_username(username, self.room_name)
            print("receive")
            if message_response:
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'username': username,
                        'room_name': self.room_name,
                        'friend_username': friend_username,
                        'msg_id': self.msg_id,
                        'notification': notification,
                    }
                )

    # Receive message from room group
    def chat_message(self, event):
        """
        This view is receive message from room group and send it into WebSocket
        """
        message = event['message']
        username = event['username']
        room_name = event['room_name']
        friend_username = event['friend_username']
        msg_id = event['msg_id']
        notification = event['notification']

        user_obj = User.objects.get(username=username)
        full_name = user_obj.first_name + " " + user_obj.last_name
        user_img_url = user_obj.photo.url
        print(full_name)
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room_name': room_name,
            'friend_username': friend_username,
            'msg_id': msg_id,
            'notification': notification,
            'full_name': full_name,
            'user_img_url': user_img_url
        }))

