from django.urls import path,include
from . import views
urlpatterns = [
    
    path('add/', views.Task_model,name='Task_model'),
    path('edit/<int:id>', views.edit_tesk,name='edit_tesk'),
    path('delete/<int:id>', views.delete_tesk,name='delete_tesk'),
   
]
