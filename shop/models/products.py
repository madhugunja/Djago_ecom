from django.db import models
from .category import Category

class Products(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='img')
    desc=models.TextField()
    price=models.IntegerField()



#static method to get the products by category id
    @staticmethod
    def get_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.objects.all()