from django.shortcuts import render
from .models import Cart,CartItem

# Create your views here.

def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    pass

def add_to_cart(request):
    pass

def remove_cartitem(request):
    pass

def update_cartitem(request):
    pass  

def checkout(request):
    pass