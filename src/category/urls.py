
from django.urls import path
from .views import  list_scholarship,search_tag, ScholarshipDetailView, scrape_data,edit_profile,form_view,generate_cv_pdf,cv, change_password
urlpatterns = [
     # path('scholarship', ScholarshipListView.as_view(), name = 'scholarship'),
     path('scholarship', list_scholarship, name = 'scholarship'),
     path('scholarship/<slug:slug>/', ScholarshipDetailView.as_view(), name='scholarship_detail'),
     path('scholarship/tag/<str:country>', search_tag, name = 'scholarship_tag'),
     # path('profile_edit/', UserEditView.as_view(), name="profile_edit"),
     path('profile_edit/', edit_profile, name="profile_edit"),
     path('change-password',change_password, name="change_password"),
     path('scrapping', scrape_data, name="scrape_data"),
     path('form/', form_view, name='form_view'),
     path('cv-form/', generate_cv_pdf, name='form_pdf'),
     path('cv',cv),
     

]
