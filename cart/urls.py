from . import views
from django.urls import path
urlpatterns = [
    path('cartdetails',views.cart_details,name='cartdetails'),
    path('addcart/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_min/<int:product_id>/',views.min_cart,name='cart_min'),
    path('cart_delete/<int:product_id>/',views.cart_delete,name='cart_delete'),
]