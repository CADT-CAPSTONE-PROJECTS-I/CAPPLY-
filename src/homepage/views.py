import uuid
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from category.models import Scholarship, Country
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from user.models import Profile
from django.core.mail import send_mail
# Create your views here.

def homepage(request):
    country_lists = Country.objects.all()
    return render(request,"homepage/home.html", {'country_lists':country_lists})


def verify_email(request, verification_token):
    profile = get_object_or_404(Profile, verification_token=verification_token)
    
    if profile.is_email_verified:
        # Email already verified, show appropriate message or redirect to a different page
        messages.info(request, 'Email already verified.')
        return redirect('home')  # Replace 'home' with your desired URL name
        
    # Mark the email as verified
    profile.is_email_verified = True
    profile.save()
    
    # Log in the user
    login(request, profile.user)
    
    # Show a success message
    messages.success(request, 'Email verified. You are now logged in!')
    
    return redirect('profile') 

  
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                
                user.is_active = False
                user.save()
                
                verification_token = str(uuid.uuid4())
                profile = Profile.objects.create(user=user, verification_token=verification_token)
                
                verification_url = request.build_absolute_uri(reverse('verify_email', args=[verification_token]))
                
                # Send the verification email
                subject = 'Email Verification'
                message = f'Please click the following link to verify your email: {verification_url}'
                from_email = 'your-email@example.com'  # Replace with your email
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)
                
                print("Account created successfully!")
                messages.success(request, 'Account created successfully!')
                return redirect('profile')  # Replace 'profile' with your desired URL name for the user's profile page
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

    else:
        return render(request, "user/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username= username, password=password)
            if user.is_staff or user.is_superuser :
                auth.login(request, user)
                messages.info(request, 'Login Successfully.')
                return redirect('admin/')
            
            elif user is not None:
                auth.login(request, user)
                messages.success(request, 'Login Successfully.')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid Credentials.')
                return redirect('login')
        except:
            messages.error(request, 'Check and login again')
            return redirect('login')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, "user/login.html", {'messages':messages})

def logout(request):
    auth.logout(request)
    
        
    return redirect('home')

@login_required
def profile(request):
    return render(request,"user/profile.html")

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class UserDeleteView(LoginRequiredMixin, View):
    template_name = 'user/delete_confirmation.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        password = request.POST.get('confirm_password', '')
        user = request.user
        if user.check_password(password):
            profile = get_object_or_404(Profile, user = user)
            profile.delete()
            user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('login') 
        else:
            messages.error(request, 'Invalid password.')
            return redirect('user_delete_confirm')

# For Category
def show_category(request):
    return render(request,"category/category.html")

# search
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        scholarships_lists = Scholarship.objects.filter(school__contains=searched).all()
        country_lists = Country.objects.all()
        context = {'searched':searched, 
                   'scholarships_lists':scholarships_lists,
                   'country_lists': country_lists}
        return render(request,'homepage/search.html', context)
                  
    else:
        return render(request, 'homepage/search.html', {})

#For aboutpage
def about(request):
    return render(request,"about/about.html")
#For contactus
def contact(request):
    return render(request,"contact/contact_us.html")
#For contactus
def contact_us(request):
    return render(request,"contact/contact_us.html")


