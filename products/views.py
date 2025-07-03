from django.shortcuts import render
from products.models import Product
# Create your views here.
def products(request):
    template_name='products/products.html'
    context={
         'products':Product.objects.all()
    }
    return render(request,template_name,context)