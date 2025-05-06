from django.contrib import admin
from .models.products import Products
from .models.category import Category
from .models.customer import Customer


# Register your models here.
class Categoryinfo(admin.ModelAdmin):
    list_display=["name"]

class Productsinfo(admin.ModelAdmin):
    list_display=["name","category","price"]
admin.site.register(Products,Productsinfo)
admin.site.register(Category,Categoryinfo)

class Customerinfo(admin.ModelAdmin):
    list_display=["first_name","last_name","email","phone_number"]
admin.site.register(Customer,Customerinfo)