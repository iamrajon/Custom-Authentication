# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(
        label='',
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name*'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Id*'})
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password*'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password**'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2')

        
        

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Id*'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password*'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

# Form for password Reset
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control"}),
    )
    
# Form for SetPassword
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    )


# Form for PasswordChange
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, "class": "form-control"}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    )
    




        

