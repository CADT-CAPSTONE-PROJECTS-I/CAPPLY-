from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Scholarship, Country
from django.core.paginator import Paginator
from django.shortcuts import render, redirect 
from django.views.generic import ListView, DetailView 
from django.template import loader
# Create your views here.

def list_scholarship(request):
    # scholarship_lists = Scholarship.objects.all().order_by('?')
    scholarship_lists = Scholarship.objects.all()
    country_lists = Country.objects.all()
    # set up pagination
    p = Paginator(Scholarship.objects.all(), 5)
    page = request.GET.get('page')
    scholarships = p.get_page(page)
    return render(request,'category/category.html',{'scholarship_lists': scholarship_lists,
    'scholarships': scholarships, 'country_lists':country_lists})

#scholarship detail views
def scholarship_detail_view(request, slug):
    scholarship_obj = None
    if slug is not None:
        try:
            scholarship_obj = Scholarship.objects.get(slug=slug)
            template = loader.get_template('category/scholarship_detail.html')
        except Scholarship.DoesNotExist:
            raise Http404
        except Scholarship.MultipleObjectsReturned:
            scholarship_obj = Scholarship.objects.filter(slug=slug).first()
            template = loader.get_template('category/scholarship_detail.html')
        except:
            raise Http404
    context = {
        'scholarship' : scholarship_obj,
    }
    return HttpResponse(template.render(context, request))

class ScholarshipDetailView(DetailView):
    model = Scholarship
    template_name = "category/scholarship_detail.html"
    


def search_tag(request, country):
    scholarships_lists = Scholarship.objects.filter(country=country)
    country_lists = Country.objects.all()
    p = Paginator(Scholarship.objects.all(), 5)
    page = request.GET.get('page')
    scholarships = p.get_page(page)
    context = {'scholarships':scholarships, 'country':country, 'country_lists':country_lists,'scholarships_lists':scholarships_lists }
    return render(request,'category/scholarship_tag_result.html', context)