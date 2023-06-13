import random
import string
from bs4 import BeautifulSoup
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import requests

from django.utils.text import slugify
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

def scrape_data(request):
    add_to_model = True  
    results = []  # List to store the scraped objects
    for i in range(1, 3):
        web_link = f'https://www.idp.com/cambodia/search/scholarship/?studyLevel=%3Aundergraduate&page={i}'
        r = requests.get(web_link)
        soup = BeautifulSoup(r.content, 'lxml')
        lists = soup.find_all('div', class_='pro_wrap')
        
        for lst in lists:
            listing = lst.find_all('div', class_='pro_list_wrap')
            
            for info in listing:
                link = info.find('a', class_='prdct_lnk').get('href')
                more_info = 'https://www.idp.com' + link
                schools = info.find('div', class_='ins_cnt')
                school = schools.a.text.strip()
                country = schools.p.text.strip().split(',')[-1].strip()
                level = info.find('div', class_='media_txt').text.strip().split('Qualification')[-1].strip()
                deadline_element = info.find('div', class_='media_btm')  # Find the deadline element
                
                if deadline_element is not None:
                    deadline = deadline_element.text.strip()  # Scrape the deadline
                else:
                    deadline = None  # Set deadline to None if element not found
                    
                allowed_chars = ''.join((string.ascii_letters, string.digits))
                slug_combine = school + " " + ''.join(random.choice(allowed_chars) for _ in range(32))
                slug = slugify(slug_combine)
                
                # Create an object or dictionary to store the scraped data
                obj = {
                    'more_info': more_info,
                    'school': school,
                    'country': country,
                    'level': level,
                    'deadline': deadline,
                    'slug': slug
                }
                
                results.append(obj)  # Append the object to the results list
    
                if add_to_model:
                    # Create a new instance of YourModel and populate it with the scraped data
                    model_instance = Scholarship(
                        more_info=more_info,
                        school=school,
                        country=country,
                        level=level,
                        deadline=deadline,
                        slug=slug
                    )
                    model_instance.save()
    if add_to_model:
        return JsonResponse({'message': 'Scrapping complete'})
    else:
        return JsonResponse(results, safe=False)

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
    def detail_filter_similar(self, **kwargs):
        context = super(ScholarshipDetailView,self).get_context_data(**kwargs)
        context['country'] = Scholarship.objects.filter(country=self.country)
        return context
    

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

# class UserEditView(generic.UpdateView):
#     form_class = EditProfileForm
#     template_name = 'user/profile_edit.html'
#     success_url = reverse_lazy('profile')
    
#     def get_object(self):
#         return self.request.user


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import EditProfileForm
from django.contrib.auth.forms import SetPasswordForm

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        password_form = SetPasswordForm(user=request.user, data=request.POST)
        
        if form.is_valid() and password_form.is_valid():
            user = form.save()
            password_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        password_form = SetPasswordForm(user=request.user)
    
    context = {
        'form': form,
        'password_form': password_form,
    }
    return render(request, 'user/profile_edit.html', context)