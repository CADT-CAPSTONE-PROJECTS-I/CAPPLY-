from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Scholarship, Country
from django.core.paginator import Paginator
from django.shortcuts import render, redirect 
from django.views.generic import ListView, DetailView 
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm

# Create your views here.

def list_scholarship(request):
    scholarships_lists = Scholarship.objects.all().order_by('?')
    country_lists = Country.objects.all()
    # set up pagination
    p = Paginator(scholarships_lists.all(), 5)
    page = request.GET.get('page')
    scholarships = p.get_page(page)
    return render(request,'category/category.html',{'scholarships_lists': scholarships_lists,
    'scholarships': scholarships, 'country_lists': country_lists})

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
    p = Paginator(scholarships_lists, 5)
    page = request.GET.get('page')
    scholarships = p.get_page(page)
    context = {'scholarships':scholarships, 
               'country':country, 
               'country_lists':country_lists,
               'scholarships_lists':scholarships_lists }
    return render(request,'category/scholarship_tag_result.html', context)
    # context = {'scholarships':scholarships, 'country':country, 'country_lists':country_lists,'scholarships_lists':scholarships_lists }
    # return render(request,'category/scholarship_tag_result.html', context)


#profile change

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user


# def scholarship_add(request, id):
#     history = History(request)
#     scholarship = Scholarship.objects.get(id=id)
#     # history = History.objects.create(scholarship=scholarship)
#     history.add(scholarship=scholarship)
#     # history.save()
#     return redirect("home")