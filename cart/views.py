from django.shortcuts import render,redirect
from .models import Cart,CartItem,Order,OrderItem
from products.models import Product
import razorpay
from electrodeal.settings import RAZORPAY_ID,RAZORPAY_SECRET


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
    request.session["cart_id"]=cart.id
    template_name="checkout.html"
    context={
        "cartitems":cart.cartitem_set.all()
    }
    return render(request,template_name,context)

def place_order(request):
    if request.method=="POST":

        cart_id=request.session.get("cart_id")
        cart=Cart.objects.get(id=cart_id)

        order=Order.objects.create(
            user=request.user,
            email=request.user.email,
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            country=request.POST.get("country"),
            zipcode=request.POST.get("zip-code")
        )

        for cartitem in cart.cartitem_set.all():
            OrderItem.objects.create(
                                      order=order,
                                      product=cartitem.product,
                                      quantity=cartitem.quantity

                                     )

        return redirect("payment",order.id)
       
def payment(request,order_id):
    client=razorpay.Client(auth=(RAZORPAY_ID,RAZORPAY_SECRET))
    data = { "amount": 500, "currency": "INR", "receipt": f'{order_id}' }
    payment=client.order.create(data=data)

    template_name="payment.html"
    context={
        "payment":payment,
        "razorpay_id":RAZORPAY_ID
    }
    return render(request,template_name,context)

    
def payment_success(request):
    template_name="payment-success.html"
    context={}
    return render(request,template_name,context)

