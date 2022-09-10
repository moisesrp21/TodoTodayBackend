from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
     # content of the todo 
     title = models.CharField(max_length=100)
     # set to current time
     created = models.DateTimeField(auto_now_add=True)
     completed = models.BooleanField(default=False)
     # assign user to this todo
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     def __str__(self):
          return self.title
