from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from shop.models.products import Products
from shop.models.category import Category
from shop.models.customer import Customer   
from django.shortcuts import render, redirect


class home(View):
    def get(self, request):
        products = Products.objects.all()
        category = Category.objects.all()  # Fetch all categories
        category_id = request.GET.get('category')  # Get the selected category from the request
        if category_id:
            products = Products.get_products_by_categoryid(category_id)  # Filter products by category ID
        else:
            products = products# Get all products if no category is selected
        return render(request, 'index.html', {'products': products, 'category': category})
    def post(self, request):
        # Handle form submission
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'signup.html', {'message': 'Passwords do not match'})

        # Check if email already exists
        if Customer.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'message': 'Email address already exists'})

        # Save user data
        try:
            Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone,
                password=password
            )
            return render(request, 'signup.html', {'message': 'Signup successful'})
        except IntegrityError:
            return render(request, 'signup.html', {'message': 'An error occurred. Please try again.'})
from django.views import View