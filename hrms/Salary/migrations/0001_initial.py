# Generated by Django 3.1.1 on 2020-12-09 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('EMP_Code', models.CharField(default='--', max_length=200)),
                ('Designatio', models.CharField(default='WCT Employee', max_length=100)),
                ('Department', models.CharField(default='WCT', max_length=200)),
                ('Month_Year', models.CharField(default='__', max_length=100)),
                ('Basic', models.IntegerField(default='--')),
                ('H_R_A', models.CharField(default='--', max_length=100)),
                ('Conc_All', models.CharField(default='--', max_length=200)),
                ('Trans_All', models.CharField(default='--', max_length=200)),
                ('CFA', models.CharField(default='--', max_length=200)),
                ('PF_Employee', models.CharField(default='--', max_length=200)),
                ('ESI_Employee', models.CharField(default='--', max_length=452)),
                ('Loan_Advance', models.CharField(default='--', max_length=500)),
                ('Tax', models.CharField(default='--', max_length=423)),
                ('Total_deduction', models.CharField(default='--', max_length=500)),
                ('Others', models.CharField(default='--', max_length=200)),
                ('Medical_Allowance', models.CharField(default='--', max_length=200)),
                ('Salary_Gross_PM', models.CharField(default='--', max_length=200)),
                ('Telephone', models.IntegerField(default='--')),
                ('Other', models.CharField(default='--', max_length=200)),
                ('Salary', models.CharField(default='--', max_length=522)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
            ],
        ),
    ]
