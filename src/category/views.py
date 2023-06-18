from io import BytesIO
import random
import string
from bs4 import BeautifulSoup
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
from django.utils.text import slugify
from .models import Scholarship, Country
from django.core.paginator import Paginator
from django.shortcuts import render, redirect 
from django.views.generic import ListView, DetailView 
from django.template import loader
from django.contrib.auth.decorators import login_required
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
                
                results.append(obj)
    
                if add_to_model:
                    country_instance, created = Country.objects.get_or_create(name = country)
                    if created:
                        country_instance.name = country
                        country_instance.save()
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


from .models import Comment, Reply
from .forms import CommentForm, ReplyForm

@login_required(login_url='login')
def create_comment(request, slug):
    scholarship = get_object_or_404(Scholarship, slug = slug)
    template_name = "category/scholarship_detail.html"
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.scholarship = scholarship
            new_comment.active = True
            new_comment.save()
            return redirect('scholarship_detail', slug=slug)
    else:
        form = CommentForm()
    
    context = {'comment_form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def create_reply(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.comment = comment
            reply.active = True
            reply.save()
            return redirect('scholarship_detail', slug=comment.scholarship.slug)
    else:
        form = ReplyForm()
    context = {'reply_form':form}
    return render(request, 'category/scholarship_detail.html', context)


def scholarship_detail(request,slug):
    scholarship = get_object_or_404(Scholarship, slug= slug)
    template_name = "category/scholarship_detail.html"
    comments = Comment.objects.filter(
        scholarship = scholarship,
        active=True)
    for comment in comments:
        replies = comment.reply_set.all()
        comment.replies = replies
    comment_form = CommentForm()
    reply_form = ReplyForm()
    context = {'reply_form':reply_form, 
               'comment_form':comment_form, 
               'comments':comments,
               'object':scholarship}
    return render(request,template_name, context)

# favorite view
from django.shortcuts import redirect, get_object_or_404
from .models import Scholarship, FavoriteScholarship, Favorited
from django.contrib.auth.decorators import login_required

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    favorited = Favorited.objects.filter(scholarship=self.object, user=self.request.user).first()
    context['favorited'] = favorited
    return context

@login_required(login_url='login')
def add_to_favorite(request, slug):
    scholarship_get = get_object_or_404(Scholarship, slug=slug)
    try:
        created= FavoriteScholarship.objects.get_or_create(user=request.user, scholarship_school=scholarship_get.school, scholarship_link = scholarship_get.slug)
        if created:
            favorited = Favorited(scholarship=scholarship_get,user=request.user,activation=True)
            favorited.save()
            return redirect('profile')
        else:
            return redirect('profile_edit')
    except IntegrityError:
        return redirect('home')
   
def favorite_list(request):
    scholarship_favorite = FavoriteScholarship.objects.all()
    return render(request,'user/favorite.html',{'scholarship_favorite':scholarship_favorite})


from django.contrib import messages
def favorite_delete(request, slug):
    try:
        favorite = FavoriteScholarship.objects.filter(scholarship_link=slug)
        favorite.delete()
    except:
        messages.info(request, 'Failed')
    return redirect('favorite')


# end of favorite view
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


def cv(request):
    return render(request,'cv.html',{})


from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from .forms import EditUserForm, EditProfileForm
from .models import Profile
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user) 
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = EditUserForm(instance=request.user)
        profile_form =EditProfileForm(instance=request.user.profile)
    context = {
        'form': form,
        'profile_form':profile_form
    }
    return render(request, 'user/profile_edit.html', context)
def change_password(request):
    if request.method == 'POST':
        password_form = SetPasswordForm(user=request.user, data=request.POST)
        
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        password_form = SetPasswordForm(user=request.user)
    
    context = {
        'password_form': password_form,
    }
    return render(request, 'user/change_password.html', context)


from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from .forms import MyForm, CVForm
from django.template.loader import render_to_string
from weasyprint import HTML
import requests
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            image = form.cleaned_data['image']
            
            # Save the uploaded image file
            fss = FileSystemStorage()
            file = fss.save(image.name, image)
            image_url = fss.url(file)
            
            # Download the image locally
            image_url_with_scheme = f"{request.scheme}://{request.get_host()}{image_url}"
            
            # Create a dictionary with the form data
            context = {'name': name, 'email': email, 'message': message, 'image_url': image_url_with_scheme}
            
            # Generate PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="form_submission.pdf"'
            
            # Render the template with the form data
            html_string = render_to_string('response.html', context)
            
            # Create the PDF from the HTML string and write it to the response
            HTML(string=html_string).write_pdf(response)

            return response
    else:
        form = MyForm()

    return render(request, 'form.html', {'form': form})

from .forms import CVForm 
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from xhtml2pdf import pisa

def generate_cv_pdf(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            summary = form.cleaned_data['summary']
            institution_name = form.cleaned_data['institution_name']
            degree_earned = form.cleaned_data['degree_earned']
            field_of_study = form.cleaned_data['field_of_study']
            dates_of_attendance = form.cleaned_data['dates_of_attendance']
            company_name = form.cleaned_data['company_name']
            job_title = form.cleaned_data['job_title']
            employment_dates = form.cleaned_data['employment_dates']
            responsibilities = form.cleaned_data['responsibilities']
            achievements = form.cleaned_data['achievements']
            skills = form.cleaned_data['skills']
            certifications = form.cleaned_data['certifications']
            project_name = form.cleaned_data['project_name']
            purpose = form.cleaned_data['purpose']
            role = form.cleaned_data['role']
            technologies_used = form.cleaned_data['technologies_used']
            outcomes = form.cleaned_data['outcomes']
            awards = form.cleaned_data['awards']
            languages = form.cleaned_data['languages']
            interests = form.cleaned_data['interests']
            references = form.cleaned_data['references']
            image_file = form.cleaned_data['image_file']

            fss = FileSystemStorage()
            file = fss.save(image_file.name, image_file)
            image_url = fss.url(file)

            image_url_with_scheme = f"{request.scheme}://{request.get_host()}{image_url}"

            context = {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
                'address': address,
                'summary': summary,
                'institution_name': institution_name,
                'degree_earned': degree_earned,
                'field_of_study': field_of_study,
                'dates_of_attendance': dates_of_attendance,
                'company_name': company_name,
                'job_title': job_title,
                'employment_dates': employment_dates,
                'responsibilities': responsibilities,
                'achievements': achievements,
                'skills': skills,
                'certifications': certifications,
                'project_name': project_name,
                'purpose': purpose,
                'role': role,
                'technologies_used': technologies_used,
                'outcomes': outcomes,
                'awards': awards,
                'languages': languages,
                'interests': interests,
                'references': references,
                'image_url': image_url_with_scheme
            }

            html_string = render_to_string('cv_template.html', context)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="form_submission.pdf"'

            pisa.CreatePDF(html_string, dest=response)

            return response
        else:
            form = CVForm()
    else:
        form = CVForm()

    return render(request, 'cv_form.html', {'form': form})


