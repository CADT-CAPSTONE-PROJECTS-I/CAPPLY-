from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def homepage(request):
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
    else:
        return render(request, "user/login.html")


def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request):
    return render(request,"user/profile.html")


# For Category
def listing_category(request):
    return render(request,"category/list_view.html")

def show_category(request):
    return render(request,"category/category.html")

