from django.urls import path
from admin_dashboard.views import *


urlpatterns = [
    path('', landing, name='admin_dashboard'),
    path('create_category/', create_new_category, name='create_category'),
    path('edit/<int:category_id>', edit_specific_category, name="edit_category"),
    path('delete/<int:category_id>', delete_specific_category, name="delete_category"),
    path('mark_featured/', mark_featured, name='mark_featured'),
    
]