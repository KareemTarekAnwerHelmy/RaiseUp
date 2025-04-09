from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .decorators import admin_required



@login_required(login_url='login')
@admin_required
def landing(request):
    return render(request, "admin_dashboard/dashboard.html")


from projects.forms import Category_ModelForm

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


from projects.models import Category, Project

@login_required(login_url='login')
@admin_required
def edit_specific_category(request, category_id):
    selected_category = Category.get_category_by_id(category_id)
    form = Category_ModelForm(instance=selected_category)
    if request.method == 'POST':
        form = Category_ModelForm(request.POST, instance=selected_category)
        if form.is_valid():
            form.save()
            return redirect('all_categories')
    return render(request, 'admin_dashboard/edit_category.html', context={"categoryForm": form})
