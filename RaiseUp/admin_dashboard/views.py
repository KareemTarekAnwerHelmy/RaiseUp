from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

@login_required(login_url='login')
@admin_required
def landing(request):
    return render(request, "admin_dashboard/dashboard.html")