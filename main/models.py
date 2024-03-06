from django.db import models

# Create your models here.

# Database object called ToDoList
class TodoItem(models.Model):
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    