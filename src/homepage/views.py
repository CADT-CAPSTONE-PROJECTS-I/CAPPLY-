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
        try:
            user = auth.authenticate(username= username, password=password)
            if user.is_staff or user.is_superuser :
                auth.login(request, user)
                messages.info(request, 'Login Successfully.')
                return redirect('admin/')
            
            elif user is not None:
                auth.login(request, user)
                messages.info(request, 'Login Successfully.')
                return redirect('profile')
            else:
                messages.info(request, 'Invalid Credentials.')
                return redirect('login')
        except:
            messages.info(request, 'Check and login again')
            return redirect('login')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, "user/login.html", {'messages.info':messages.info})


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





import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer,pagesize=letter, bottomup=0)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    textob = p.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica", 14)
    scholarships = Scholarship.objects.all()
    lines=[]
    
    for scholarship in scholarships:
        lines.append(scholarship.school)
        lines.append(scholarship.level)
        lines.append(scholarship.slug)
        # lines.apppend("/n")
    
    for line in lines:
        textob.textLine(line)
        
    p.drawText(textob)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")