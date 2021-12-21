from django import forms

class pl_register_form(forms.Form):
    manager_name = forms.CharField(error_messages = {'required' : 'Please enter Manager Name'}, label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'Manager Name'
        }
    ))
    address = forms.CharField(error_messages = {'required' : 'Please enter Address of Parking Lot'}, label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'Parking Lot Address'
        }
    ))
    city = forms.CharField(error_messages = {'required' : 'Please enter City of Parking Lot'}, label = '', widget=forms.TextInput(
        attrs={
            'placeholder' : 'City',
        }
    ))
    booking_price = forms.IntegerField(error_messages = {'required' : 'Please enter Booking Price'}, label = '', widget=forms.NumberInput(
        attrs={
            'placeholder' : 'Slot Booking price'
        }
    ))
    opening_time = forms.TimeField(error_messages = {'required' : 'Please enter opening time'}, label = '', widget=forms.TimeInput(
        attrs={
            'placeholder' : 'Parking Lot Opening TIme'
        }
    ))
    closing_time = forms.TimeField(error_messages = {'required' : 'Please enter closing time'}, label = '', widget=forms.TimeInput(
        attrs={
            'placeholder' : 'Parking Lot Closing TIme'
        }
    ))
    email = forms.EmailField(error_messages = {'required' : 'Please enter valid email id'}, label = '', widget=forms.EmailInput(
        attrs={
            'placeholder' : 'Email id'
        }
    ))
    total_slot_count = forms.IntegerField(error_messages = {'required' : 'Please enter total available slots'}, label = '', widget=forms.NumberInput(
        attrs={
            'placeholder' : 'Total available slots'
        }
    ))
    