from django.db import models
# Create your models here.
from Employee.models import Employee
class Employee_Salary(models.Model):
    Name=models.ForeignKey(Employee, on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    EMP_Code=models.CharField(max_length=200,default='--')
    Designatio=models.CharField(max_length=100,default='WCT Employee')
    Department=models.CharField(max_length=200,default='WCT')
    Month_Year=models.CharField(max_length=100,default='__')
    Basic=models.IntegerField(default='--')
    H_R_A=models.CharField(max_length=100,default='--')
    Conc_All=models.CharField(max_length=200,default='--')
    Trans_All=models.CharField(max_length=200,default='--')
    CFA=models.CharField(max_length=200,default='--')
    PF_Employee=models.CharField(max_length=200,default='--')
    ESI_Employee=models.CharField(max_length=452,default='--')
    Loan_Advance=models.CharField(max_length=500,default='--')
    Tax=models.CharField(max_length=423,default='--')
    Total_deduction=models.CharField(max_length=500,default='--')
    Others=models.CharField(max_length=200,default='--')
    Medical_Allowance=models.CharField(max_length=200,default='--')
    Salary_Gross_PM=models.CharField(max_length=200,default='--')
    Telephone=models.IntegerField(default='--')
    Other=models.CharField(max_length=200,default='--')
    Salary=models.CharField(max_length=522,default='--')


    def __str__(self):
        return str(self.Name)+str(self.Month_Year)