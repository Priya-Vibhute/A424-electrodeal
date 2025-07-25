from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product,through='CartItem')

    class Meta:
        db_table="cart"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=0)

    class Meta:
        db_table="cart_item"

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(null=False)
    address=models.CharField(max_length=50,null=False)
    city=models.CharField(max_length=50,null=False)
    country=models.CharField(max_length=50,null=False)
    zipcode=models.PositiveIntegerField()
    product=models.ManyToManyField(Product,through="OrderItem")
    is_paid=models.BooleanField(default=False)
    quantity=models.PositiveIntegerField(default=0)

    class Meta:
        db_table="order"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=0)

    class Meta:
        db_table="order_item"

