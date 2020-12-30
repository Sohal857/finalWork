from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django_countries.fields import CountryField
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password','confirm_password')
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name' : forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('website','company','phone_number','unit','street_number','street_name','city','state','zip_code','country')
        labels  = {
            'unit':'Appartment/Unit no',
            'state':'State/Province',
        }
        widgets = {

            'website' : forms.TextInput(attrs={'placeholder': 'Website address'}),
            'company' : forms.TextInput(attrs={'placeholder': 'Company name'}),
            'phone_number' : forms.TextInput(attrs={'placeholder': 'Mobile/Phone no.'}),
            'unit': forms.TextInput(attrs={'placeholder': 'Unit'}),
            'street_number' : forms.TextInput(attrs={'placeholder': 'Street number'}),
            'street_name' : forms.TextInput(attrs={'placeholder': 'Street name'}),
            'city': forms.TextInput(attrs={'placeholder': 'City name'}),
            # 'state' : forms.TextInput(attrs={'placeholder': 'State/Province name'}),
            'zip_code' : forms.TextInput(attrs={'placeholder': 'Zip/Postal code'}),

        }
