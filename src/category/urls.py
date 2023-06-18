
from django.urls import path
<<<<<<< HEAD
from .views import  list_scholarship,search_tag, scholarship_detail, scrape_data,edit_profile,form_view,generate_cv_pdf,cv, change_password, create_reply, create_comment
=======
from .views import  list_scholarship,search_tag, ScholarshipDetailView, scrape_data,edit_profile,form_view,generate_cv_pdf,cv, change_password
from .views import  list_scholarship,search_tag, ScholarshipDetailView, add_to_favorite, favorite_list,favorite_delete
>>>>>>> 31fe35e09f90e64e6d04f8ae040c719456d71093
urlpatterns = [
     # path('scholarship', ScholarshipListView.as_view(), name = 'scholarship'),
     path('scholarship', list_scholarship, name = 'scholarship'),
     path('scholarship/<slug:slug>/', scholarship_detail, name='scholarship_detail'),
     path('scholarship/tag/<str:country>', search_tag, name = 'scholarship_tag'),
     # path('profile_edit/', UserEditView.as_view(), name="profile_edit"),
     path('profile_edit/', edit_profile, name="profile_edit"),
     path('change-password',change_password, name="change_password"),
     path('scrapping', scrape_data, name="scrape_data"),
     path('form/', form_view, name='form_view'),
     path('cv-form/', generate_cv_pdf, name='form_pdf'),
     path('cv',cv),
<<<<<<< HEAD
     path('comment/<slug:slug>', create_comment, name="create_comment"),
     path('reply/<int:comment_id>', create_reply, name="create_reply"),
     # path('comment-reply/<slug:slug>',create_comment_or_reply, name="create_comment_or_reply")
     
=======
     # favorite url
     path('add-to-favorite/<slug:slug>/', add_to_favorite, name='add_to_favorite'),
     path('favorite',favorite_list,name='favorite' ),
     path('favorite-delete/<slug:slug>', favorite_delete, name="favorite_delete")
     # end of favorite url
>>>>>>> 31fe35e09f90e64e6d04f8ae040c719456d71093

]
