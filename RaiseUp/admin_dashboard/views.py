from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

from projects.forms import Category_ModelForm


@login_required(login_url='login')
@admin_required
def landing(request):
    return render(request, "admin_dashboard/dashboard.html")



@login_required(login_url='login')
@admin_required
def create_new_category(request):
    form = Category_ModelForm()
    if request.method == 'POST':
        form = Category_ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'admin_dashboard/dashboard.html')
    return render(request, 'admin_dashboard/create_category.html', context={"categoryForm": form})