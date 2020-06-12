from django.db import models

# Create your models here.
'''
class Destination:
    id : int
    name : str
    img : str
    descp : str
    price : int
    offer : bool
'''
class Destination(models.Model):
    name = models.CharField(max_length = 200,default =True)
    img = models.ImageField(upload_to = 'MyPics',default = True)
    descp = models.TextField(default = True)
    price = models.IntegerField(default = True)
    offer = models.BooleanField(default = False)