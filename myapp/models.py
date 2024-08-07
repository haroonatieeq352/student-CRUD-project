from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)

    def __self__(self):
        return self.name
    
