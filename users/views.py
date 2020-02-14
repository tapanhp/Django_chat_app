import requests
import constants
from utils import get_user_object, generate_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from notification.models import Notifications
from .models import User


# Register the user with user's given information
def registration(request):
    """
    This method registers a new user and sends OTP.

    personal information of users are first name, last name, username, email, password, phone number & image.
    """
    if request.method == 'POST':

        # get user's personal information

        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pswd']
        password2 = request.POST['cpswd']
        cont = request.POST['phn']
        image = request.FILES.get('photo')

        if password == password2:  # compare password & confirm password

            if User.objects.filter(username=user_name).exists():  # check username duplication
                messages.error(request, constants.duplicate_username)
                return redirect('registration')

            else:

                if User.objects.filter(email=email).exists():  # check email duplication
                    messages.error(request, constants.duplicate_email)
                    return redirect('registration')

                elif User.objects.filter(phone=cont).exists():  # check phone number duplication
                    messages.error(request, constants.duplicate_phone_no)
                    return redirect('registration')

                else:  # here send OTP in given phone number
                    url = "https://2factor.in/API/V1/728bad74-85f5-11e9-ade6-0200cd936042/SMS/" + cont + "/AUTOGEN/OTPSEND"
                    response = requests.request("GET", url)
                    data = response.json()
                    request.session['otp_session_data'] = data['Details']
                    request.session['mobile'] = cont

                    # register the user with user's personal information

                    user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name,
                                                    email=email, password=password, phone=cont, photo=image)
                    user.save()

                    # show the message of OTP sent

                    cont = "*****" + cont[5:]
                    msg = 'Your OTP sent to mobile number ending with ' + cont + '.'
                    messages.success(request, msg)

                    # redirect on otpverify.html page for OTP verification

                    return redirect('otpverify')

        else:  # if password & confirm password does not match then show the error message and redirect on registration page.
            messages.error(request, constants.wrong_confirm_password)
            return redirect('registration')

    else:
        return render(request, 'users/registration.html')


# Verify entered OTP and redirect on login page
def otp_verification(request):
    """
    This view is use for OTP verification. It will call api which is use for Verify the OTP. If
    OTP will does not match then it will raise wrong OTP error in screen and if there will no any error then first of all
    it will change the is_verified field of that user in database from False to True.

    Then it will create one notification room for users which room will use when anyone send message to this user.

    Then it will redirect on login.html page for login in chat_app.
    """

    if request.method == "POST":
        user_otp = request.POST['otp']

        # call api for verify the OTP and get response message from that.

        url = "https://2factor.in/API/V1/728bad74-85f5-11e9-ade6-0200cd936042/SMS/VERIFY/" + request.session[
            'otp_session_data'] + "/" + user_otp
        response = requests.request("GET", url)
        data = response.json()
        mobile = request.session['mobile']
        user = User.objects.get(phone=mobile)

        # check response status

        if data['Status'] == "Success":
            user.is_verified = True
            user.save()

            # create room for notification

            random_string = generate_random_string(7)
            notify_room = Notifications.objects.create(user=user, room=random_string)
            notify_room.save()
            return redirect('login')  # redirect on login.html page

        else:
            messages.error(request, constants.wrong_otp)  # show wrong OTP message
            return redirect('otpverify')  # redirect on otpverify.html page

    else:
        return render(request, 'users/otpverify.html')


# user will login here
def login(request):
    """
    This view is logs in the user.
    :return if User is already logged in or provides valid credential then home page else login page.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user_name = request.POST['uname']
        password = request.POST['pswd']
        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, constants.invalid_credentials)
            return redirect('login')

    else:
        return render(request, 'users/login.html')


# user will logout here
@login_required
def logout(request):
    """
    This view logs out the user.
    :return redirects to login view
    """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, constants.success_logged_out)
        return redirect('login')


# get logged in user profile data
@login_required
def profile(request):
    """
    This view returns all the data of logged in user.

    :return: html page named profile.html with context(data-type: dictionary) of user's data
    """
    user = get_user_object(request.user.username)
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)


# update profile of the user
@login_required
def update_profile(request):
    """
    This view updates user details.

    :return: html page named profile.html
    """

    if request.method == 'POST':

        # get updated user's information from profile.html page

        username = request.POST['uname']
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        image = request.FILES.get('photo')

        if User.objects.filter(username=username).exclude(id=request.user.id):  # check username duplication
            messages.error(request, constants.duplicate_username)
            return redirect('profile')

        elif User.objects.filter(email=email).exclude(id=request.user.id):  # check email duplication
            messages.error(request, constants.duplicate_email)
            return redirect('profile')

        else:  # update user's information
            if image is None:
                User.objects.filter(phone=request.user.phone).update(username=username, first_name=firstname,
                                                                     last_name=lastname, email=email)
            else:
                user = User.objects.get(phone=request.user.phone)
                user.photo = image
                user.username = username
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.save()
            messages.success(request, constants.success_profile_update)
            return redirect('profile')  # after successfully update the profile redirect on same profile.html page
    else:
        return render(request, 'users/profile.html')


# get other friends personal information
@login_required
def user_profile(request, username):
    """
    This view returns details of a user based on username.

    :param username: this username will be used to get the information of that user.
    :return: html page named profile.html with context(data-type: dictionary) of user's data
    """

    user = get_user_object(username)
    context = {
        'user': user
    }
    return render(request, 'users/user_profile.html', context)


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError(constants.wrong_forgot_email)
        return email
