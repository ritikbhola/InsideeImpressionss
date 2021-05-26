from django.db import models 

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    description = models.TextField(max_length=400,default="",blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class order(models.Model):
    name1 = models.CharField(max_length=100)
    email1 = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=12)
    description1 = models.TextField(max_length=400,default="",blank=True)
    image = models.ImageField(upload_to='images', default="")
    date = models.DateField()

    def __str__(self):
        return self.name1