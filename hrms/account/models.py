from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from Employee.models import Employee
from django.contrib.auth.models import User

# class UserProfile(models.Model):
#         # This field is required.
#         user = models.OneToOneField(User,on_delete=User.CASHCADE)
#         # These fields are optional
#         mobile=models.CharField(max_length=50)
#
#         def __unicode__(self):
#                 return self.user.username




class Emp_Bank_Detail(models.Model):
    EName=models.ForeignKey(Employee, on_delete=models.CASCADE)
    Emp_Code=models.CharField(max_length=100,default='wct000')
    Bankname=models.CharField(max_length=50,default=None)
    Account_NO=models.CharField(max_length=100,default=None)
    IFSC_Code=models.CharField(max_length=100,default=None)
    Branch=models.CharField(max_length=100,default=None)
    Registerd_Mobile=models.CharField(max_length=30,default=None)
    GooglePayNo=models.CharField(max_length=100,default=None)
