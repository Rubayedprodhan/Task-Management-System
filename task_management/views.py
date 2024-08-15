# from django.shortcuts import render,redirect
# from task_category.models import Category
# from task_model.models import ModelF
# def home(request):
#     task_model=ModelF.objects.all()
#     task_category=Category.objects.all()
#     context={
#         'task_model':task_model,
#         'task_category':task_category

#     }
#     return render(request, 'home.html', context)  
from django.shortcuts import render, redirect
from task_category.models import Category
from task_model.models import ModelF

def home(request):
    task_model = ModelF.objects.all()
    task_category = Category.objects.all()
    context = {
        'task_model': task_model,
        'task_category': task_category
    }
    return render(request, 'home.html', context)
