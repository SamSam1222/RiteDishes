from django import forms
from .models import Comment
from .models import AboutUs
from .models import Food, User
from django.contrib.auth.models import User
from RiteWeb.models import UserProfileInfo
from django.contrib.auth.forms import  UserCreationForm

# from django.contrib.auth.forms import UserCreationForm





class About(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = AboutUs
        fields = ('image', 'title', 'body')

        

class CommentForm(forms.ModelForm):
    Commenter = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your name'
        }))
    body = forms.CharField(max_length=100, widget = forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Comment here', 'rows':3
    }))
    class Meta:
        model = Comment
        fields = ['Commenter', 'body']
        

        

class CustormerForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = None


    class Meta:
        model = User
        fields = ('username', 'email', )
   
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),


        }

        labels = {
            'password1':'Password',
        }


class UserProfileInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Customer_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta():
        model = UserProfileInfo
        fields = ('username','phone_number', 'Customer_location')

        labels = {
            'location':'Your Location',
        }

    widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'Customer_location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),


        }
