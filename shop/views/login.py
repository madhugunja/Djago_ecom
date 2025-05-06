from django.shortcuts import render
from django.http import HttpResponse
from shop.models.products import Products
from shop.models.category import Category
from shop.models.customer import Customer   
from django.shortcuts import render, redirect
from django.views import View
from django.db import IntegrityError

class login(View):  
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        # Handle form submission
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email and password match a user in the database
        try:
            customer = Customer.objects.get(email=email, password=password)
            return redirect('/')
        except Customer.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid email or password'})
        

