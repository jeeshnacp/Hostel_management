import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from app.models import Login, Hostel, Student, Parent, Food, Complaint, Staff, Fees, Notification, BookRoom, Payment


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
        model = Hostel
        fields = ('total_rooms', 'occupied','annual_expenses', 'location', 'contact_no', 'room_facilities')


class studentregister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Student
        fields = ('name', 'address', 'contact_no', 'email', 'image')


class parentregister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Parent
        fields = ('name', 'address', 'child_name', 'contact_no', 'email')


class foods(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('breakfast', 'lunch', 'dinner')


class complaintsform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('subject', 'date', 'complaint')


class staffform(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'age', 'address', 'contact_no', 'email')


class feesform(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    room_rent = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    mess_bill = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Fees
        fields = ('student', 'from_date', 'to_date', 'room_rent', 'mess_bill')


class notificationform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notification
        fields = ('notification', 'date')


class StudentBookRoomForm(forms.ModelForm):
    date_joining = forms.DateField(widget=DateInput)

    class Meta:
        model = BookRoom
        fields = ('date_joining',)


MONTH_CHOICES = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),

)


def current_year():
    return datetime.date.today().year


def year_choice():
    return [(r, r) for r in range(2021, datetime.date.today().year + 10)]


class PayBillForm(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='please Enter a Valid Card no')])
    card_cvv = forms.CharField(validators=[RegexValidator(regex='^.{3}$', message='please Enter a Valid cvv')])
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES)
    expiry_year = forms.TypedChoiceField(coerce=int, choices=year_choice, initial=current_year)

    class Meta:
        model = Payment
        fields = ('card_no', 'card_cvv','expiry_month', 'expiry_year')


class bill_form(forms.ModelForm):
    class Meta:
        model=Fees
        fields=('student','amount')
