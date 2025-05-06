from django.urls import path
from .views import signup
from .views import login    
from .views import home
from django.views import View
from django.db import IntegrityError
from django.urls import path
from .views.cart import  add_to_cart, cart_page, remove_from_cart



urlpatterns = [
    path('', home.home.as_view(), name='home'),
    path('signup', signup.signup.as_view(), name='signup'),
    path('login', login.login.as_view(), name='login'),
    path('cart/', cart_page, name='cart_page'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_page, name='cart_page'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
   
]
