from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import Login, hostel


class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)

class hostelform(forms.ModelForm):
    class Meta:
        model=hostel
        fields=('name','place','contact_no','email')
