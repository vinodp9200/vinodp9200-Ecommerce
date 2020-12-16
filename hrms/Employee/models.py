from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('', 'Select Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Depart_Choice=(

        ('','Select Your Department'),
        ('Web Design & Development','Web Design & Development'),
        ('Digital Marketing','Digital Marketing'),
        ('Sales Team','Sales Team'),
        ('Human Resource','Human Resource'),
        ('Other','Other'),
    )
    Laptop_Choice=(
        ('','Office Laptop'),
        ('y','Yes'),
        ('n','No')
    )
    Blood_Choice=(
        ('','Blood Group'),
        ('O+','O+'),
        ('O-','O-'),
        ('B+','B+'),
        ('B-','B-'),
        ('A+','A+'),
        ('A-','A-'),
        ('AB+','AB+'),
        ('Ab-','AB-'),

    )
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=50,)
    mobile=models.IntegerField(unique=True)
    address=models.TextField()
    gender =models.CharField(choices=GENDER_CHOICES, max_length=8)
    email =models.EmailField(unique=True)
    blood_group=models.CharField(choices=Blood_Choice,max_length=50)
    department=models.CharField(choices=Depart_Choice,max_length=100)
    designation=models.CharField(max_length=100)
    laptop=models.CharField(choices=Laptop_Choice,max_length=10)
    salary=models.CharField(max_length=100,default='0000..')
    password=models.CharField(max_length=100)

    # class Meta:
    #     managed = True
    #     db_table='employee'
    def __str__(self):
        return self.name






