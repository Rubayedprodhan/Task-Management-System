from django.db import models
from django.utils import timezone

from task_category.models import Category
# Create your models here.
class ModelF(models.Model):
    task_title=models.CharField(max_length=40)
    task_description=models.CharField(max_length=40)
    is_completed=models.BooleanField(default=False)
    task_assint_date=models.DateTimeField(default=timezone.now)
    
    categories = models.ManyToManyField(Category, related_name='tasks')

    def __str__(self):
        return self.task_title

  