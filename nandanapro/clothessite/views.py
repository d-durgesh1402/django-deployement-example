from django.shortcuts import render
from clothessite.forms import UserForm,UserInfoForm

from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
import json
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from clothessite.models import Subscriber
from clothessite.forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import get_object_or_404
# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        return render(request, 'clothessite/signup.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'clothessite/signup.html', {'form': SubscriberForm()})
def confirm(request):
    sub = get_object_or_404(Subscriber,email=request.GET.get('email',False))
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'clothessite/signup.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'clothessite/signup', {'email': sub.email, 'action': 'denied'})
def delete(request):
    sub = get_object_or_404(Subscriber,email=request.GET.get('email',False))
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'clothessite/signup.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'clothessite/signup.html', {'email': sub.email, 'action': 'denied'})
def location(request):
    return render(request,'clothessite/location.html')
def returnrule(request):
    return render(request,'clothessite/returnrule.html')
def privacy(request):
    return render(request,'clothessite/privacy.html')
def shipping(request):
    return render(request,'clothessite/shipping.html')
def index(request):
    return render(request,'clothessite/index.html')
def westerndress(request):
    return render(request,'clothessite/westerndress.html')
def sareedress(request):
    return render(request,'clothessite/sareedress.html')
def indiandress(request):
    return render(request,'clothessite/indiandress.html')
def indowesterndress(request):
    return render(request,'clothessite/indowesterndress.html')
def startuppage(request):
    return render(request,'clothessite/startuppage.html')
def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return render(request,'clothessite/index.html')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'clothessite/user_login.html', {})
@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
def registration(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        userinfo_form=UserInfoForm(data=request.POST)
        if user_form.is_valid() and userinfo_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            info=userinfo_form.save(commit=False)
            info.user=user
            info.save()
            registered=True
            return render(request,'clothessite/index.html')

        else:
            print(user_form.errors,userinfo_form.errors)
    else:
        user_form=UserForm()
        userinfo_form=UserInfoForm()
    return render(request,'clothessite/registration.html',
                           {'user_form':user_form,
                             'userinfo_form':userinfo_form,
                              'registered':registered})
def contactus(request):
    return render(request,'clothessite/contactus.html')
