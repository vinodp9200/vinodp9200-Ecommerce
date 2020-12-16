from django import forms
from .models import Employee
class Emp_LoginForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=[
            'email','password'
        ]

class PasswordChangeForms(forms.ModelForm):
    class Meta:
        model=Employee
        fields=[
             'email','password'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }







class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['name','mobile','address','gender','email','blood_group','department','designation','laptop','password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class changePasswordForm(forms.Form):
     oldPassword=forms.CharField(label='Enter Old Password',max_length=50 ,min_length=5)
     newpassword1=forms.CharField(label='Enter New Updated Password',max_length=50,min_length=5)
     newpassword2=forms.CharField(label='Repeat Your New Password',max_length=50,min_length=5)



