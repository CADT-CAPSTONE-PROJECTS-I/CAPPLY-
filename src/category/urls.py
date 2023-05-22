
from django.urls import path
from .views import  list_scholarship
urlpatterns = [
     # path('scholarship', ScholarshipListView.as_view(), name = 'scholarship'),
     path('scholarship', list_scholarship, name = 'scholarship'),
    #  path('scholarship/<slug:slug>', scholarship_detail, name='scholarship_detail'),
     # path('scholarship/<slug:slug>', ScholarshipDetailView.as_view(), name='scholarship_detail'),
]