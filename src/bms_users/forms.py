from django import forms

class signupform(forms.Form):
    name = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'Name'
        }
    ))
    username = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'username'
        }
    ))
    phonenumber = forms.CharField(label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'phone-number with country code and +',
        }
    ), initial='+91')
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