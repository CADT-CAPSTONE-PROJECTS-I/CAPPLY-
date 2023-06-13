
from django.urls import path, re_path
from .views import  list_scholarship,search_tag, ScholarshipDetailView, scrape_data,edit_profile
urlpatterns = [
     # path('scholarship', ScholarshipListView.as_view(), name = 'scholarship'),
     path('scholarship', list_scholarship, name = 'scholarship'),
     path('scholarship/<slug:slug>/', ScholarshipDetailView.as_view(), name='scholarship_detail'),
     path('scholarship/tag/<str:country>', search_tag, name = 'scholarship_tag'),
     # path('profile_edit/', UserEditView.as_view(), name="profile_edit"),
     path('profile_edit/', edit_profile, name="profile_edit"),
     path('scrapping', scrape_data, name="scrape_data")

]
