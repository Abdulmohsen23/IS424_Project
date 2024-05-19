from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Item

class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Maximum 8 characters and Must not be fully numeric"
        self.fields['password2'].help_text = 'Your Password must match with the above password'
        self.fields['username'].help_text = ''
        self.fields['phone_number'].help_text = 'Maximum 10 digits allowed'
    class Meta:
        model = Profile
        fields = ['username', 'password1', 'password2', 'phone_number']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'created_date', 'quantity']
        widgets = {
            'created_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ItemUpdationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'created_date', 'quantity']
        widgets = {
            'created_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
