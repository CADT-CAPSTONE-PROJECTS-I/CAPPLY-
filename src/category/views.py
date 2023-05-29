from django.forms import SlugField
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Scholarship, Profile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect 
from django.views.generic import ListView, DetailView 

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

#scholarship detail views
def scholarship_detail_view(request, slug=None):
    scholarship_obj = None
    if slug is not None:
        try:
            scholarship_obj = Scholarship.objects.get(slug=slug)
        except Scholarship.DoesNotExist:
            raise Http404
        except Scholarship.MultipleObjectsReturned:
            scholarship_obj = Scholarship.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": scholarship_obj,
    }
    return render(request, "category/scholarship_detail.html", context=context)

def scholarship_detail_view1(request, slug):
    q = Scholarship.objects.filter(slug__iexact = slug)
    if q.exists():
       q = q.first()
    else:
       return HttpResponse('<h1>Post Not Found</h1>')
    context = {
 
       'post': q
   }
    return render(request, 'category/scholarship_detail.html', context)

class ScholarshipDetailView(DetailView):
    model = Scholarship
    template_name = "category/scholarship_detail.html"