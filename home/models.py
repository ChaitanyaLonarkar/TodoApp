from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskData(models.Model):
  user=models.ForeignKey(User, on_delete=models.SET_NULL, null= True , blank= True) 
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  #if user deleted from website then all data will be remove when on_delete=models.CASCADE
  TaskTitle = models.CharField(max_length=255)
  TaskDesc = models.TextField(max_length=2550)
  Curr_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.TaskTitle

