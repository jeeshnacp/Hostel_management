import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from app.models import Login, hostel, student, parent, food, complaint, staff, fees


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is not valid number')


class DateInput(forms.DateInput):
    input_type = 'date'


class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)


class hostelform(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = hostel
        fields = ('total_rooms', 'occupied', 'annual_expenses', 'location', 'contact_no', 'room_facilities')


class studentregister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = student
        fields = ('name', 'address', 'contact_no', 'email','image')


class parentregister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = parent
        fields = ('name', 'address', 'child_name', 'contact_no', 'email')


class foods(forms.ModelForm):
    class Meta:
        model = food
        fields = ('breakfast', 'lunch', 'dinner')


class complaintsform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ('subject', 'date', 'complaint')


class staffform(forms.ModelForm):
    class Meta:
        model = staff
        fields = ('name', 'age', 'address', 'contact_no', 'email')


class feesform(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)

    class Meta:
        model = fees
        fields = ('student', 'from_date', 'to_date', 'room_rent', 'mess_bill')
