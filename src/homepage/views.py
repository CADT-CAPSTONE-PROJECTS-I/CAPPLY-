from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from category.models import Scholarship, Country
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.

def homepage(request):
    country_lists = Country.objects.all()
    return render(request,"homepage/home.html", {'country_lists':country_lists})


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

def profile(request):
    return render(request,"user/profile.html")

def profile_edit(request):
    return render(request,"user/profile_edit.html")

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





