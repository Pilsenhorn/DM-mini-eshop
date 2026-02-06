from django.shortcuts import render, redirect
from .models import Lead


def landing_page(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            Lead.objects.get_or_create(
                email=email,defaults={"source": "landing"}
            )

        return redirect("thank_you")
    
    return render(request, "leads/landing.html")

def thank_you(request):
    return render(request, "leads/thank_you.html")