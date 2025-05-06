from django.shortcuts import render
from django.http import HttpResponse
from .models.products import Products
from .models.category import Category
from .models.customer import Customer   
from django.shortcuts import render, redirect
from 

# Create your views here.
def home(request):
    products = Products.objects.all()
    category = Category.objects.all()  # Fetch all categories
    category_id = request.GET.get('category')  # Get the selected category from the request
    if category_id:
        products = Products.get_products_by_categoryid(category_id)  # Filter products by category ID
    else:
        products = products# Get all products if no category is selected
    return render(request, 'index.html', {'products': products, 'category': category})

# filepath: [views.py](http://_vscodecontentref_/4)
from django.db import IntegrityError

def signup(request):
    if request.method == 'POST':
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

    # Render the signup form for GET requests
    return render(request, 'signup.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')  # Use .get() to access POST data
        password = request.POST.get('password')  # Use .get() to access POST data
        users = Customer.objects.filter(email=email, password=password)
        if users.exists():
            # Redirect to the home page after successful login
            return redirect('/')
        else:
            # Show an error message for invalid credentials
            return render(request, 'login.html', {'message': 'Invalid email or password'})
        
def cart_page(request):
    if request.method == 'GET':
        return render(request, 'cart.html')


    
    

@staticmethod
def get_customer_by_email(email):
    try:
        return Customer.objects.get(email=email)
    except Customer.DoesNotExist:
        return None
