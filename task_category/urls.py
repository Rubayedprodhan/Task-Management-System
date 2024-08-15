from django.urls import path,include
from . import views 
urlpatterns = [
   
    path('add/', views.category,name='category'),
    #path('task_category', include('task_category.urls')),
]