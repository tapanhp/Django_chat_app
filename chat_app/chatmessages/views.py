import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from notification.models import SentFriendRequest
from chatmessages.models import ChatMessage
from django.utils.safestring import mark_safe
from friends.models import Friends
from django.db.models import Q
from notification.models import Notifications
from utils import get_user_object, get_chat_messages


# load chat screen
@login_required
@csrf_exempt
def chatscreen(request):
    """
    This view returns last 10 messages between logged in user and the other user.

    :return: http response with response data which required for show chat screen
    """
    if request.method == "POST":

        # get user objects

        logged_in_user = get_user_object(request.user.username)
        friend_obj = get_user_object(request.POST.get('username'))

        # get friend full name and profile image from friend user object

        full_name = friend_obj.first_name + " " + friend_obj.last_name
        profile_pic_src = str(friend_obj.photo.url)

        # get chats between current user and their friend

        sent_messages = get_chat_messages(logged_in_user, friend_obj)
        recevied_messages = get_chat_messages(friend_obj, logged_in_user)

        all_chats_list = [[m.message, str(m.sent_at), 'sent'] for m in sent_messages]
        for r in recevied_messages:
            all_chats_list.append([r.message, str(r.sent_at), 'received'])

        # get room name for do chat

        room_obj = Friends.objects.filter(user1=logged_in_user, user2=friend_obj)
        if room_obj:
            room_name = Friends.objects.get(user1=logged_in_user, user2=friend_obj).room_name
        else:
            room_name = Friends.objects.get(user1=friend_obj, user2=logged_in_user).room_name

        all_chats_list.sort(key=lambda x: x[1])  # sort chat in ascending order as per datetime

        # if there are more than 10 messages then get last 10 message otherwise get all messages and append 'same_date'
        # or 'new_date' at last index of all_chat for identify that new date start from that message

        same_day = False
        if len(all_chats_list) > 10:
            if all_chats_list[-11][1].split(' ')[0] == all_chats_list[-10][1].split(' ')[0]:
                same_day = True
            all_chats_list = all_chats_list[-10:]

        if len(all_chats_list):
            all_chats_list[0].append('same_date')

        for i, chat in enumerate(all_chats_list):
            if not i == len(all_chats_list) - 1:
                if not all_chats_list[i][1].split(' ')[0] == all_chats_list[i + 1][1].split(' ')[0]:
                    all_chats_list[i + 1].append('new_date')
                    if not len(all_chats_list[i]) == 4:
                        all_chats_list[i].append('same_date')
                else:
                    if not len(all_chats_list[i]) == 4:
                        all_chats_list[i].append('same_date')
            else:
                if not len(all_chats_list[i]) == 4:
                    all_chats_list[i].append('same_date')

        friend_notify_room = Notifications.objects.get(user=friend_obj).room

        response_data = {
            "name": full_name,
            "profile-pic": profile_pic_src,
            "messages": all_chats_list,
            'room_name_json': mark_safe(json.dumps(room_name)),
            'room_name': room_name,
            'user_name': request.user.username,
            'friend_notify_room': friend_notify_room,
            'same_day': same_day,
            'friend_id': friend_obj.id,
        }
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


# load home page of chat_app
@login_required
@csrf_exempt
def chat_app(request):
    """
    This view will return recent chats, count of unread messages, count of friend
    request.

    :return: http response with response data which required for load home page
    """

    # get logged in user object & get all users except admin users

    logged_in_user = get_user_object(request.user.username)
    all_users = User.objects.filter(is_staff=False)

    add_contact_list = []

    # get count of received friend request and accepted friend request

    sent_friend = SentFriendRequest.objects.filter(
        Q(receiver=logged_in_user) & Q(receiver_accepted=False) & Q(seen_requests=False)).count()
    notification = SentFriendRequest.objects.filter(
        Q(sender=logged_in_user) & Q(receiver_accepted=True) & Q(seen_notifications=False)).count()

    # get list of accepted request by friends

    accepted_request_list = SentFriendRequest.objects.filter(sender=logged_in_user, receiver_accepted=True).order_by('-accepted_at')

    # get remain all contacts who are not in friend list, their's request are not pending and their's request yet we have not received

    for user in all_users:
        sent_friend_request_obj = SentFriendRequest.objects.filter(sender=logged_in_user, receiver=user)
        received_friend_request_obj = SentFriendRequest.objects.filter(sender=user, receiver=logged_in_user)

        if not sent_friend_request_obj and not received_friend_request_obj and not user.username == logged_in_user.username:
            add_contact_list.append(user)

    friend_request_list = SentFriendRequest.objects.filter(receiver=logged_in_user, receiver_accepted=False)
    all_friends = Friends.objects.filter(Q(user1=logged_in_user) | Q(user2=logged_in_user), friends=True)
    all_room = [friend.room_name for friend in all_friends]  # get all room names

    recent_chat = []
    friend_list = []
    all_friends_objs = []
    no_conversion = []

    for friend in all_friends:
        if not friend.user1.username == logged_in_user.username:
            friend_list.append(friend.user1.username)
            all_friends_objs.append(friend.user1)
        else:
            friend_list.append(friend.user2.username)
            all_friends_objs.append(friend.user2)

    # get unread message count and get recent chats

    for friend in friend_list:
        friend_obj = get_user_object(friend)
        friends_chats = ChatMessage.objects.filter(
            Q(sender=friend_obj, receiver=logged_in_user) | Q(sender=logged_in_user, receiver=friend_obj)).order_by(
            '-sent_at')

        unread_msgs = ChatMessage.objects.filter(sender=friend_obj, receiver=logged_in_user, message_seen=False)
        unread_msg_count = len(unread_msgs)

        if friends_chats:
            recent_chat.append(
                [friend_obj.first_name + " " + friend_obj.last_name, friends_chats[0].message, friends_chats[0].sent_at,
                 friend_obj.username, str(friend_obj.photo.url), friend_obj, unread_msg_count])
        else:
            no_conversion.append([friend_obj.first_name + " " + friend_obj.last_name, "", "", friend_obj.username,
                                  str(friend_obj.photo.url), friend_obj, unread_msg_count])

    recent_chat.sort(key=lambda x: x[2])  # sort recent chat as per ascending order by datetime
    recent_chat.reverse()
    recent_chat = recent_chat + no_conversion

    room_name = 'test_room'
    all_room.append(room_name)

    notify_room = Notifications.objects.get(user=logged_in_user).room  # get room name

    print(*accepted_request_list)

    context = {
        'logged_in_user': logged_in_user,
        'all_users': all_users,
        'all_friends_objs': all_friends_objs,
        'add_contact_list': add_contact_list,
        'friend_request_list': friend_request_list,
        'accepted_request_list': accepted_request_list,
        'room_name_json': mark_safe(json.dumps(room_name)),
        'all_room': all_room,
        'user_name': str(request.user.username),
        'notify_room': str(notify_room),
        'recent_chat': recent_chat,
        'sent_friend_count': sent_friend,
        'notification_count': notification
    }
    return render(request, 'users/chat_app.html', context)


# load previous 10 messages of chat
@login_required
@csrf_exempt
def load_more_chat(request):
    """
    This method is use for load previous 10 messages when scroll top on chat screen

    :return: http response with response data which required for load next 10 messages
    """
    # get scroll count for identify how many time did scroll top

    scroll_count = request.POST.get('scroll_count')

    # get logged in user and friend object

    logged_in_user = get_user_object(request.user.username)
    friend_obj = get_user_object(request.POST.get('username'))

    # get all chat between logged in user and their friend

    sent_messages = get_chat_messages(logged_in_user, friend_obj)
    recevied_messages = get_chat_messages(friend_obj, logged_in_user)

    all_chats_list = [[m.message, str(m.sent_at), 'sent'] for m in sent_messages]

    for r in recevied_messages:
        all_chats_list.append([r.message, str(r.sent_at), 'received'])

    all_chats_list.sort(key=lambda x: x[1])  # sort chat as per ascending order of datetime

    # get previous 10 messages

    message_load_count = (int(scroll_count) + 1) * 10

    if message_load_count >= len(all_chats_list):
        if (message_load_count - len(all_chats_list)) > 10:
            load_messages = []
            next_message = "False"
        else:
            load_messages = all_chats_list[:-(int(scroll_count)) * 10]
            next_message = "True"
            more_messages = False
    else:
        load_messages = all_chats_list[-(message_load_count):-(message_load_count) + 10]
        next_message = "True"
        more_messages = True

    load_messages.reverse()

    # append 'same_date' or 'new_date' string at last index of load message list for identify that new date start from that message

    for i, msg in enumerate(load_messages):
        if not i == len(load_messages) - 1:
            if not load_messages[i][1].split(' ')[0] == load_messages[i + 1][1].split(' ')[0]:
                load_messages[i].append('new_date')
            else:
                load_messages[i].append('same_date')
        else:
            if more_messages:
                if not load_messages[i][1].split(' ')[0] == all_chats_list[-(message_load_count) - 1][1].split(' ')[0]:
                    load_messages[i].append('new_date')
                else:
                    load_messages[i].append('same_date')
            else:
                load_messages[i].append('new_date')

    response_data = {
        "scroll_count": int(scroll_count) + 1,
        "load_messages": load_messages,
        "next_message": next_message,
    }
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


@login_required
@csrf_exempt
def check_date(request):
    response_data = {
        "check": 'check',
    }
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


# seen single chat message

@login_required
@csrf_exempt
def seen_message(request):
    """
    This method marks a message as seen.
    :return: http response with response data success.
    """
    message_id = request.POST.get('message_id')
    message_obj = ChatMessage.objects.get(id=message_id)
    message_obj.message_seen = True
    message_obj.save()

    response_data = {
        "success": 'success',
    }
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


# seen all messages

@login_required
@csrf_exempt
def seen_all_message(request):
    """
    This view marks all the messages between two users as seen.

    :return: http response with response data success.
    """

    # get user objects

    logged_in_user = get_user_object(request.user.username)
    friend_obj = get_user_object(request.POST.get('username'))

    # get unseen chat messages between logged in user and their friend and then make it all unseen chat messages to seen.

    chat_messages = ChatMessage.objects.filter(sender=friend_obj, receiver=logged_in_user, message_seen=False)

    for msg in chat_messages:
        msg.message_seen = True
        msg.save()

    response_data = {
        "success": 'success',
    }
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
