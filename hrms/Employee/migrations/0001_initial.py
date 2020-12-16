# Generated by Django 3.1.1 on 2020-12-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(unique=True)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('', 'Select Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=8)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('blood_group', models.CharField(choices=[('', 'Blood Group'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('Ab-', 'AB-')], max_length=50)),
                ('department', models.CharField(choices=[('', 'Select Your Department'), ('Web Design & Development', 'Web Design & Development'), ('Digital Marketing', 'Digital Marketing'), ('Sales Team', 'Sales Team'), ('Human Resource', 'Human Resource'), ('Other', 'Other')], max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('laptop', models.CharField(choices=[('', 'Office Laptop'), ('y', 'Yes'), ('n', 'No')], max_length=10)),
                ('salary', models.CharField(default='0000..', max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
