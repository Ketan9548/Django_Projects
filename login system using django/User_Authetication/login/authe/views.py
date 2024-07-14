from base64 import urlsafe_b64encode
from . tokens import generate_tokens
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from login import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
# from django.utils.encoding import force_str
from django.core.mail import EmailMessage,send_mail


# Create your views here.

@csrf_exempt
def index(request):
    return render(request, "static/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]


        if User.objects.filter(username=username):
            messages.error(request,"Username is already exist! please try some other Username")
            return redirect('index')
        
        if User.objects.filter(email=email):
            messages.error(request,"Email is already register")
            return redirect('index')
        
        if len(username)>8:
            messages.error(request,'username must be under 8 charactor')

        if pass1 != pass2:
            messages.error(request,"Password didn't match!")
        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account has been successfully created. we have send you a confirmation email, Please confirm your email address in order to activate your account.")


        # welcome email

        subject = 'Welcome to Shop Login - User Login!!'
        message = 'Hello' + myuser.first_name+'!! \n'+'welcome to Our Sotore \n Thanks You for Visiting our website \n We have have also send you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking You\n Kapil Chauhan'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently = True)
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid':urlsafe_b64encode(force_bytes(myuser.pk)),
            'token': generate_tokens.make_token(myuser),
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect("signin")
       
        
    return render(request, "static/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request ,'static/index.html',{'fname':fname})
        else:
            messages.error(request,'Bad Request')
            return redirect('index')
    
    return render(request, "static/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged Out SuccessFully!")
    return render(request, "static/index.html")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_tokens.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('index')
    else:
        return render(request, 'activation_failed.html')
