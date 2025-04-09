from django.urls import path
from admin_dashboard.views import landing, create_new_category, delete_specific_category, edit_specific_category, mark_featured


urlpatterns = [
    path('', landing, name='admin_dashboard'),
    
]