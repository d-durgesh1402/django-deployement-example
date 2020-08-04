from django import forms
from django.contrib.auth.models import User
from clothessite.models import UserInfo
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class UserInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=('Contact_No','Address')
class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))        
