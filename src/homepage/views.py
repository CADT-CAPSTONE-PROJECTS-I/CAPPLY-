from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from category.models import Scholarship

# Create your views here.

def homepage(request):
    # if request.user.is_authenticated:
    #     if request.user.is_staff or request.user.is_superuser:
    #         return redirect('admin/')
    #     else:
    #         return render(request,"homepage/home.html")
    # else:
        return render(request,"homepage/home.html")


def register(request):    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        confirm_password = request.POST['confirm_password']
        if password ==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is not availble')
                return redirect(register)
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, password=password, email=email)
                user.set_password(password)
                user.save()
                print("Account created successfully!")
                return redirect('login')

    else:
        return render(request, "user/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password=password)
        if user.is_staff or user.is_superuser :
            auth.login(request, user)
            return redirect('admin/')
        
        elif user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Invalid Credentials.')
            return redirect('login')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, "user/login.html")


def logout(request):
    auth.logout(request)
    return redirect('home')
import scraping

def profile(request):
    return render(request,"user/profile.html")

def profile_edit(request):
    return render(request,"user/profile_edit.html")

# For Category
def listing_category(request):
    return render(request,"category/list_view.html")

def show_category(request):
    return render(request,"category/category.html")

# search

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        scholarships = Scholarship.objects.filter(school__contains=searched)
        return render(request,'homepage/search.html', {'searched':searched, 
                                                       'scholarships':scholarships}
                  )
    else:
        return render(request, 'homepage/search.html', {}
                  )
    
#For aboutpage
def about(request):
    return render(request,"about/about.html")

#For contactus
def contact_us(request):
    return render(request,"contact/contact.html")

