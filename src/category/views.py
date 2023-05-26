from django.shortcuts import render
from .models import Scholarship
from django.core.paginator import Paginator
from django.shortcuts import render, redirect  
from profile.forms import ProfileForms  
from profile.models import Profile  
# Create your views here.

def list_scholarship(request):
    # scholarship_lists = Scholarship.objects.all().order_by('?')
    scholarship_lists = Scholarship.objects.all()
    # set up pagination
    p = Paginator(Scholarship.objects.all(), 20)
    page = request.GET.get('page')
    scholarships = p.get_page(page)
    return render(request,'category/category.html',{'scholarship_lists': scholarship_lists,
    'scholarships': scholarships})

#profile views
