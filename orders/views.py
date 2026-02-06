from django.shortcuts import render
from .forms import OrderCreateForm
from .models import Order, OrderItem
from . services import get_or_create_user_from_order
from products.models import Product

def order_create_view(request):
    #simulation cart
    product = Product.objects.filter(is_active=True).first()

    if not product:
        return render(request, "orders/empty.html")
    
    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            # soft user
            user = get_or_create_user_from_order(
                email=form.changed_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name",]
            )

            #order

            order = Order.objects.create(
                user=user,
                email=form.changed_data["email"],
                note=form.cleaned_data["note"],
                shipping_methods="Personal contact",
                shipping_price=0,
            )

            # order items
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=1,
                price=product.price,
            )

            return redirect("order_succes")
    
    else:
        form = OrderCreateForm()

    return render(request, "orders/checkout.html", {"form": form})

def order_succes_view(request):
    return render(request, "orders/succes.html")