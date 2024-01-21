# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUserProfile
from django.core.mail import send_mail, BadHeaderError
from Custom_Authentication.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
import random
import string


# function for generationg random otp
def generate_random_otp():
    empty = ""
    otp = empty.join(random.choices(string.digits, k=6))
    return otp

# function for sending mail for otp verification
def send_otp_mail(receiver_email, otp):
    subject = "OTP verification"
    message = f"Dear User, \n\n Your OTP for Email Verification is: {otp}"
    email_from = EMAIL_HOST_USER
    guest_email = receiver_email

    print(f"otp: {otp}, host_email: {email_from}, rec_email: {guest_email}")
    try:
        send_mail(subject, message, email_from, [guest_email], fail_silently=True)
        print(f"Email sent successfully")
        return True
    except BadHeaderError as e:
        return HttpResponse("Invalid Header Found!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# view function for User Registration
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        form = CustomUserCreationForm(request.POST)
        print(f"email: {email}")
        if form.is_valid():
            user = form.save()

            # generate otp
            otp = generate_random_otp()

            # save otp in CustomUserProfile model
            CustomUserProfile.objects.create(user=user, otp=otp, is_email_verified = False)

            # calling send_otp_mail function for sending mail
            if send_otp_mail(email, otp):
                return redirect('verify-otp', name=user.name)
                # Reverse the url and Append the 'name' parameter
                # name = user.name
                # url = reverse('verify-otp', kwargs={"name": name})
                # return redirect(url)
            else:
                return render(request, "templates/signup.html", {"error": None, "form": form})       
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

# function based view for otp verification
login_required(login_url="log-in")
def verify_otp_view(request, name):
    user_profile = CustomUserProfile.objects.get(user__name=name)

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        if entered_otp == user_profile.otp:
            user_profile.is_email_verified = True
            user_profile.save()
            messages.success(request, "Account Verified successfully, You can login now!")
            return redirect('log-in')
        else:
            return render(request, "templates/verify.html", {"error": "Invalid otp, please recheck your email", "user": {'name': name}})
    else:
        context = {'user': {'name': name}}
        return render(request, "templates/verify.html", context)
    

# function based view for user login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # extracting current CustomUserProfile
            current_user_profile = CustomUserProfile.objects.get(user__email=email)
            if current_user_profile.is_email_verified == True:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Change 'home' to your home URL
                else:
                    messages.error(request, 'Invalid login credentials.')
            else:
                return render(request, "templates/login.html", {'form': form, "error": "Your Email is not Verified, please check your email to get otp and vefify your account then only you can login!"})
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url="log-in")
def logout_view(request):
    logout(request)
    return redirect('home')  # Change 'login' to your login URL

def home_view(request):
    context = {}
    return render(request, "home.html", context)
