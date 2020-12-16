from django import forms
from .models import emp_Leave

class EmployeeLeaveFrom(forms.ModelForm):
    class Meta:
        model=emp_Leave
        fields='__all__'
