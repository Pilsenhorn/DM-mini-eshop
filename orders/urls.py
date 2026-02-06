from django.urls import path
from .views import order_create_view, order_succes_view

urlpatterns = [
    path("checkout/", order_create_view, name="order_create"),
    path("succes/", order_succes_view, name="order_succes"),
]