from django.urls import path
from . import views
urlpatterns = [
    path('',views.view_cart,name="cart") ,
    path('add-to-cart/<int:productid>',views.add_to_cart,name='add-to-cart'),
    path('remove-cartitem/<int:cartitem_id>',views.remove_cartitem,name="remove-cartitem"),
    path('update-cartitem/<int:cartitem_id>',views.update_cartitem,name="update-cartitem"),
    path('checkout',views.checkout,name="checkout"),
    path('place-order',views.place_order,name="place-order"),
    path('payment/<int:order_id>',views.payment,name="payment"),
    path('payment-success',views.payment_success,name="payment-success")
]
