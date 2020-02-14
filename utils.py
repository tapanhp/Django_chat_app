import string
import random
from users.models import User
from chatmessages.models import ChatMessage
from notification.models import SentFriendRequest


# get user object

def get_user_object(username):
    """ This method is use for get user object with the help of username from User model

    :param username: this will use for get user object from user model
    :return: user object
    """
    user = User.objects.get(username=username)
    return user


# get chat messages list

def get_chat_messages(sender, receiver):
    """ This method is use for get chat messages between that two friend (sender and receiver)

    :param sender: user object
    :param receiver: user object
    :return: chat messages list
    """
    chat_msgs_list = ChatMessage.objects.filter(sender=sender, receiver=receiver).order_by('sent_at')
    return chat_msgs_list


# get friend request list

def get_friend_requests_list(sender, receiver):
    """ This method is use for get friend request list of the users

    :param sender: user object
    :param receiver: user object
    :return: friend requests list
    """
    friend_req_list = SentFriendRequest.objects.filter(sender=sender, receiver=receiver, receiver_accepted=False)
    return friend_req_list


# create random string

def generate_random_string(length):
    """ This method is use for generate random string of given length.

    :param length: this is require for set length of random string
    :return: random string of given length
    """
    letters = string.ascii_letters
    random_string = "".join(random.choice(letters) for i in range(length))

    return random_string
