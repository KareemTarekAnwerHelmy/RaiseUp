from django.urls import path
from admin_dashboard.views import *


urlpatterns = [
    path('', landing, name='admin_dashboard'),
    path('create_category/', create_new_category, name='create_category'),
    
]