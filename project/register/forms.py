from django import forms

class User(forms.Form):
     first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    user_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(null=True, blank=True)
    email_id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    