from django.shortcuts import render,redirect
from .models import Cart,CartItem,Order
from products.models import Product


# Create your views here.

def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    total=0
    for cartitem in cart.cartitem_set.all():
        total+=cartitem.quantity*cartitem.product.price

    template_name="cart.html"
    context={
        "cartitems":cart.cartitem_set.all(),
        "total":total
    }
    return render(request,template_name,context)

def add_to_cart(request,productid):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cartitem,cartitem_created=CartItem.objects.get_or_create(cart=cart,product=Product.objects.get(id=productid))
    if cartitem_created:
        cartitem.quantity=1
    else:
        cartitem.quantity+=1
    cartitem.save()
    return redirect("products")

def remove_cartitem(request,cartitem_id):
    cartitem=CartItem.objects.get(id=cartitem_id)
    cartitem.delete()
    return redirect("cart")

def update_cartitem(request,cartitem_id):
    if request.method=="POST":
      cartitem=CartItem.objects.get(id=cartitem_id)
      quantity=request.POST.get("quantity")
      cartitem.quantity=quantity
      cartitem.save()
      return redirect("cart")
    

def checkout(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    template_name="checkout.html"
    context={
        "cartitems":cart.cartitem_set.all()
    }
    return render(request,template_name,context)

def place_order(request):
    if request.method=="POST":
        order=Order.objects.create(
            user=request.user,
            email=request.user.email,
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            country=request.POST.get("country"),
            zipcode=request.POST.get("zip-code")
        )

        return redirect("payment")
       
def payment(request):
    template_name="payment.html"
    context={}
    return render(request,template_name,context)

    