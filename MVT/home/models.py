from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.name