from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models  import *

GEEKS_CHOICES =(
    ("01", "1 декабря"),
    ("02", "2 декабря"),
    ("03", "3 декабря"),
    ("04", "4 декабря"),
    ("05", "5 декабря"),
    ("06", "6 декабря"),
    ("07", "7 декабря"),
    ("08", "8 декабря"),
    ("09", "9 декабря"),
    ("10", "10 декабря"),
    ("11", "11 декабря"),
    ("12", "12 декабря"),
    ("13", "13 декабря"),
    ("14", "14 декабря"),
    ("15", "15 декабря"),
    ("16", "16 декабря"),
    ("17", "17 декабря"),
    ("18", "18 декабря"),
    ("19", "19 декабря"),
    ("20", "20 декабря"),
    ("21", "21 декабря"),
    ("22", "22 декабря"),
    ("23", "23 декабря"),
    ("24", "24 декабря"),
    ("25", "25 декабря" ),
    ("26", "26 декабря"),
    ("27", "27 декабря"),
    ("28", "28 декабря"),
    ("29", "29 декабря"),
    ("30", "30 декабря"),
    ("31", "31 декабря"),
)
class AddPostForm(forms.Form):
    digit = forms.ChoiceField(choices=GEEKS_CHOICES, label="Выберите число декабря" )

class RegisterUserForm1(UserCreationForm):
    username = forms.CharField(label='Логин', required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', required=False, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',  required=False, widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class Skills(forms.Form):
    name = forms.CharField(label='Назввние', max_length=50)
    pic = forms.ImageField(label='Фотка')


