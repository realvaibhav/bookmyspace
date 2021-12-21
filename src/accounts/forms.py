from django.contrib.auth import get_user_model
from django import forms

user = get_user_model()

class signupform(forms.Form):
    name = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'Name'
        }
    ))
    phonenumber = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'phone-number with country code and +',
        }
    ), initial='+91')
    username = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'username'
        }
    ))
    password = forms.CharField(label = '', widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'create password'
        }
    ))
    confirm_password = forms.CharField(label = '', widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'Confirm password'
        }
    ))

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = user.objects.filter(username_iexact=username)
    #     if qs.exists():
    #         raise forms.ValidationError("This username already exists")
    #     return username

    # def clean_phonenumber(self):
    #     phonenumber = self.cleaned_data.get("phonenumber")
    #     qs = user.objects.filter(phonenumber_iexact=phonenumber)
    #     if qs.exists():
    #         raise forms.ValidationError("This phonenumber already exists")
    #     return phonenumber




class loginform(forms.Form):
    username = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'username'
        }
    ))
    password = forms.CharField(label = '', widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'password'
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = user.objects.filter(username=username)
        if not qs.exists():
            raise forms.ValidationError("This username does'nt exists")
        return username