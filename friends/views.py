import json
import requests
import datetime
import constants
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from notification.models import SentFriendRequest, Notifications
from friends.models import Friends
from django.http import HttpResponse
from django.db.models import Q
from utils import get_user_object, get_friend_requests_list, generate_random_string


# give list of contacts

@login_required
def add_contact(request):
    """
    This view is return all contacts list which contacts are not in user's friend list or not in user's pending
    requests list.

    :return: render to html page named add_friend.html with context (type: dictionary)
    """

    # get user objects

    logged_in_user = get_user_object(request.user.username)
    all_users = User.objects.filter(is_staff=False)

    add_contact_list = []
    sent_request_list = []
    notifications_room_list = []

    # get all contacts which are not in friend list

    for user in all_users:

        received_friend_request_obj = get_friend_requests_list(user, logged_in_user)
        friend_obj = Friends.objects.filter(Q(user1=logged_in_user, user2=user) | Q(user2=logged_in_user, user1=user))
        if (not received_friend_request_obj) and (not user == logged_in_user) and (not friend_obj):
            add_contact_list.append(user)
            notification_room_obj = Notifications.objects.get(user=user)
            notifications_room_list.append(notification_room_obj.room)
        # get contacts whose we already sent requests

        sent_friend_request_obj = get_friend_requests_list(logged_in_user, user)
        if sent_friend_request_obj:
            sent_request_list.append(user)

        context = {
            'add_contact_list': add_contact_list,
            'sent_request_list': sent_request_list,
            'notifications_room_list': notifications_room_list,
        }

    return render(request, 'users/add_friend.html', context)


# invite to friend

@login_required
def invite_contact(request):
    """
    This view is used to invite user's new friend to join this chat_app
    It will use TwoFactor API for invite new contact
    """
    if request.method == 'POST':
        invite_contact = request.POST['invitecontact']
        logged_user = request.user.first_name + " " + request.user.last_name
        message = logged_user + " " + constants.invite_msg
        user = User.objects.filter(phone=invite_contact)

        if user:
            messages.error(request, constants.invite_number_exists)
            return redirect(reverse('addcontact'))

        else:
            invite_contact = int(invite_contact)
            payload = {"From": "Chat Application", "Msg": message, "To": invite_contact}
            response = requests.request("POST", constants.invite_sms_api, data=json.dumps(payload))
            messages.success(request, constants.success_invite)
            return redirect(reverse('addcontact'))


# sent friend request

@login_required
@csrf_exempt
def add_friend(request):
    """
    This view is sent request to new contact. It will create object of SentFriendRequest model and
    delete that object when cancel that request.

    :return: http response with response data which will use for sent and cancel request
    """
    if request.method == "POST":
        logged_in_user = get_user_object(request.user.username)
        friend_obj = get_user_object(request.POST.get('username'))
        request_btn_value = request.POST.get('request_btn_value').strip()
        print(request_btn_value)

        if request_btn_value == 'Add Friend':  # sent request
            send_request = SentFriendRequest.objects.create(sender=logged_in_user, receiver=friend_obj)
            send_request.save()
            req_btn_title = 'Request Sent'
            cancel_request = False

        elif request_btn_value == 'Request Sent':  # cancel that request
            delete_request = SentFriendRequest.objects.get(sender=logged_in_user, receiver=friend_obj)
            delete_request.delete()
            req_btn_title = 'Add Friend'
            cancel_request = True

        notification_obj = Notifications.objects.get(user=friend_obj)
        friend_notification_room = notification_obj.room

        response_data = {
            "req_btn_title": req_btn_title,
            "friend_notification_room": friend_notification_room,
            "cancel_request": cancel_request,
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return render(request, "users/add_friend.html")


@login_required
def friend_request(request):
    logged_in_user = get_user_object(username=request.user.username)
    all_users = User.objects.filter(is_staff=False)

    sent_friend = SentFriendRequest.objects.filter(
        Q(receiver=logged_in_user) & Q(receiver_accepted=False) & Q(seen_requests=False))
    sent_friend.update(seen_requests=True)

    notifications_room_list = []
    received_friend = []

    for user in all_users:
        received_friend_request_obj = SentFriendRequest.objects.filter(sender=user, receiver=logged_in_user,
                                                                       receiver_accepted=False)
        if received_friend_request_obj:
            received_friend.append(user)
            notification_room_obj = Notifications.objects.get(user=user)
            notifications_room_list.append(notification_room_obj.room)

    context = {
        'friend_request': received_friend,
        'notifications_room_list': notifications_room_list,
    }
    return render(request, 'users/friend_request.html', context)


# accept friend request here

@login_required
@csrf_exempt
def accept_request(request):
    """
    This view is accept new friend request.  And then it will create one unique room name for chat.
    It will create object of friend model

    :return: http response with response data success
    """
    if request.method == "POST":

        # get users objects

        logged_in_user = get_user_object(request.user.username)
        friend_obj = get_user_object(request.POST.get('username'))

        # create unique room name for do chat on that room

        random_string = generate_random_string(5)
        room_name = logged_in_user.first_name + "_" + friend_obj.first_name + "_" + random_string

        # create new friend object

        create_friend = Friends.objects.create(user1=logged_in_user, user2=friend_obj, room_name=room_name)
        create_friend.save()

        # update sent request object

        sent_request_obj = SentFriendRequest.objects.get(sender=friend_obj, receiver=logged_in_user)
        sent_request_obj.receiver_accepted = True
        sent_request_obj.accepted_at = datetime.datetime.now()
        sent_request_obj.save()

        notification_obj = Notifications.objects.get(user=friend_obj)
        friend_notification_room = notification_obj.room

        response_data = {
            "Response": 'Success',
            "friend_notification_room": friend_notification_room,
            "logged_in_users_username": logged_in_user.username
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


# decline request here

@login_required
@csrf_exempt
def decline_request(request):
    """
    This view is decline request of new friend.
    It will delete object of SentFriendRequest model.

    :return: http response with response data success
    """
    if request.method == "POST":
        logged_in_user = get_user_object(request.user.username)
        friend_obj = get_user_object(request.POST.get('username'))

        # delete sent request object

        delete_sent_request_obj = SentFriendRequest.objects.get(sender=friend_obj, receiver=logged_in_user)
        delete_sent_request_obj.delete()

        notification_obj = Notifications.objects.get(user=friend_obj)
        friend_notification_room = notification_obj.room

        response_data = {
            "Response": 'Success',
            "friend_notification_room": friend_notification_room,
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


@login_required
@csrf_exempt
def notification_seen(request):
    if request.method == "POST":
        logged_in_user = get_user_object(username=request.user.username)
        sent_friend = SentFriendRequest.objects.filter(
            Q(sender=logged_in_user) & Q(receiver_accepted=True) & Q(seen_notifications=False))

        sent_friend.update(seen_notifications=True)
        response_data = {
            "Response": 'Success',
        }
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
