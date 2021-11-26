from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    # with PasswordInput html tag will treat tag as password type
    password = forms.CharField(widget=forms.PasswordInput)
