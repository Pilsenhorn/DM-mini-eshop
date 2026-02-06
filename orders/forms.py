from django import forms

class OrderCreateForm(forms.Form):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(max_length=100, label="First name")
    last_name = forms.CharField(max_length=100, label="Last name")

    phone = forms.CharField(max_length=30, required=False, label="Phone")

    street = forms.CharField(max_length=255, label="Street")
    city = forms.CharField(max_length=100, label="City")
    zip_code = forms.CharField(max_length=20, label="ZIP code")

    note = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label="Note"
    )