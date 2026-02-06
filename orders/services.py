from django.contrib.auth.models import User


def get_or_create_user_from_order(email, first_name="", last_name=""):
    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "username": email,
            "first_name": first_name,
            "last_name": last_name,
            "is_active": True,
        }
    )
    return user
