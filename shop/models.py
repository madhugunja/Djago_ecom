from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    # category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='img')
    desc=models.TextField()
    price=models.IntegerField()
 