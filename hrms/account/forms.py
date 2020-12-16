from django import forms
from .models import Emp_Bank_Detail
from django.contrib.auth.models import User


class EmpAccountForm(forms.ModelForm):
    class Meta:
        model=Emp_Bank_Detail
        fields='__all__'


class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]