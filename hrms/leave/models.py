from django.db import models
from Employee.models import Employee
from django.contrib.auth.models import User
# Create your models here.
class emp_Leave(models.Model):
    Reporting_Choice = (
        ('', 'Select to Report'),
        ('H', 'HR'),
        ('t', 'TL'),
        ('m', 'MD'),
    )
    application_type = (
        ('', 'Select Leave Type'),
        ('m', 'Sick Leave'),
        ('e', 'Emergency Leave'),
        ('p', 'Paid Leave'),
        ('u', 'Unpaid Leave')
    )
    Name = models.CharField(max_length=500)
    Date = models.DateTimeField()
    Employee_Code = models.CharField(max_length=50)
    Email = models.EmailField()
    Address = models.TextField()
    Application_Type = models.CharField(choices=application_type, max_length=5)
    From = models.CharField(max_length=20)
    To = models.CharField(max_length=52)
    Department = models.CharField(choices=Reporting_Choice, default='HR', max_length=10)

