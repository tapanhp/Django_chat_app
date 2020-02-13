from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
import json
from users.models import User
from .models import SentFriendRequest

# @login_required
# def addfriend(request):
#
#     if request.method == "POST":
#         print(request.POST.get('username'))
#
#         response_data = {"Test": "test"}
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
    # try:
    #     friend_obj = User.objects.get(username=username)
    # except:
    #     return HttpResponseNotFound()
    #
    # logged_in_user = User.objects.get(username=request.user.username)
    #
    # try:
    #     send_request_obj = SentFriendRequest.objects.create(sender=logged_in_user, receiver=friend_obj)
    #     send_request_obj.save()
    # except:
    #     return HttpResponseNotFound(status=500)
    #
    # all_users = User.objects.all()
    #
    # context = {
    #     'logged_in_user': logged_in_user,
    #     'all_users': all_users,
    # }
    # return render(request, 'users/chat_app.html')
