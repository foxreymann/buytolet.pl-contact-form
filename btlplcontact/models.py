from django.db import models

# Create your models here.
class ContactData(models.Model):

  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  email = models.EmailField()


