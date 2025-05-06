from urllib import request
from django.shortcuts import redirect, render
from django.http import JsonResponse
from shop.models.products import Products
from shop.models.category import Category



class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add_to_cart(self, product_id, quantity):
        if str(product_id) in self.cart:
            self.cart[str(product_id)] += quantity
        else:
            self.cart[str(product_id)] = quantity
        self.session['cart'] = self.cart  # Save the cart in the session
        self.session.modified = True 


    

def cart_page(request):
    cart = Cart(request)
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.cart.items():
        product = Products.objects.get(id=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity
        })
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id=None):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Get product_id from the form
        quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1 if not provided
        cart = Cart(request)
        cart.add_to_cart(product_id, quantity)
    return redirect('cart_page')  # Redirect to the cart page
def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Get product_id from the form
        cart = Cart(request)
        if str(product_id) in cart.cart:
            del cart.cart[str(product_id)]  # Remove the product from the cart
            cart.session['cart'] = cart.cart  # Save the updated cart in the session
    return redirect('cart_page')  # Redirect to the cart page