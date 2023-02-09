
from django import forms


# each attribute indicates the name of a <input> tag in <form> of HTML
class UserForm(forms.Form):
    # widget=forms.TextInput: <input type='text' />
    # label indicates the value of <label for:>, which is the id of connected <input>
    # attrs indicates the varied attributes of <label>
    username = forms.CharField(label='User', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'autofocus': ''}))

    # widget=forms.PasswordInput: <input type='password' />
    password = forms.CharField(label='Password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class RegisterForm(forms.Form):
    g = (('m', 'male'), ('f', 'female'))
    username = forms.CharField(label='User', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'autofocus': ''}))
    password1 = forms.CharField(label='Password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='Repeat', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'please repeat your password'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    gender = forms.ChoiceField(label='Gender', choices=g)

