from django.shortcuts import render,redirect
from .forms import EmployeeLeaveFrom
from django.core.mail import send_mail
from Employee.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
# @login_required(login_url='/index')
def emp_Leave(request):
    form=EmployeeLeaveFrom(request.POST or None)
    if form.is_valid():
        sender=form.cleaned_data['Email']
        Aname=form.cleaned_data['Applicant_Name']
        Employee_Code=form.cleaned_data['Employee_Code']
        applicationt=form.cleaned_data.get('Application_Type')
        frm=form.cleaned_data['From']
        to=form.cleaned_data['To']
        deprt=form.cleaned_data.get('Department')
        subject=applicationt
        message=str('Leave: types:'+applicationt)+str('\nApplicant_Name: '+Aname)+str('\nEmployee_Code'+Employee_Code)+\
                str('\nFrom'+frm)+str('To'+to)+str('\nReporting Department'+deprt)
        recipients = ['webtechnovinod@gmail.com',sender]
        send_mail(subject, message, sender, recipients)
        form.save()

    username= request.session.get('emp')
    print('name =', username)
    context = {'username': username,'form':form }
    return render(request,'dashboard/empleave.html',context)

def emp_Logout(request):
    logout(request)
    return redirect('/userlog')


