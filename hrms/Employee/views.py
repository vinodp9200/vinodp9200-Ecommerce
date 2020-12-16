from django.shortcuts import render,redirect,HttpResponse
from .models import Employee
import csv
from django.contrib import messages
from .forms import NewEmployeeForm,changePasswordForm,Emp_LoginForm
from django.http import FileResponse
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeForms
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
def add_Employee(request):
    form=NewEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('hellow')
    context={
        'form':form
    }
    return render(request,'adduser.html',context)
# Create your views here
def dash_Bord(request):
    emp = request.session.get('emp')
    digital= Employee.objects.filter(department='Digital Marketing').count()
    webde= Employee.objects.filter(department='Web Design & Development').count()
    sales= Employee.objects.filter(department='Sales Team').count()
    hr= Employee.objects.filter(department='Human Resource').count()
    context={'webdevelopment':webde,'sales':sales,'degital':digital,'hr':hr}
    return render(request,'dashboard/dashboard_index.html',context)

def index(request):
    if request.method=='POST':
        uid=request.POST.get('email')
        passw=request.POST.get('psw')
        user=Employee.objects.filter(email=uid,password=passw)
        if user:
            request.session['emp']=passw
            request.session['email']=uid
            return redirect('/dashbord')
        else:

            return render(request, 'index.html')

    return render(request,'index.html')

def download(request):
    resopnce = HttpResponse(content_type='text/csv')
    resopnce['Content-Disposition'] = 'attachment; filename=WCTEmployee.csv'
    writer = csv.writer(resopnce)
    writer.writerow(['Name','Code','Mobile','Address','Gender','Email','Blood Group','Department'
                     'Designation','Laptop','salary'])
    emp = request.session.get('emp')
    empdata = Employee.objects.all().filter(password=emp)
    for data in empdata:
        writer.writerow([data.name,data.code,data.mobile,data.address,data.gender,
                         data.blood_group,data.department,data.designation,data.laptop,data.salary])

    return resopnce
def changePassw(request):
    if request.method == 'POST' or None:
            name=request.POST.get('uname')
            pass1=request.POST.get('psw')
            pass2=request.POST.get('psw1')
            user=Employee.objects.filter(name=name)and pass1==pass2
            if user:

                messages.success(request,'Password Updated Successfully !')
                return redirect('/userlog')
            else:
                messages.error(request,'Pleae Enter Currect Info')
                return redirect('/changepass')

    else:
         return render(request, 'changepass.html')

def updateinfo(request):
    emp = request.session.get('emp')
    empdata=Employee.objects.all().filter(password=emp)
    context={'all_employee':empdata}
    return render(request,'update.html',context)

def edit(request,id):
    empObj =Employee.objects.get(pk=id)
    form =NewEmployeeForm(request.POST or None, instance=empObj)
    if form.is_valid():
        form.save()
        return redirect('/show')
    context ={
       'form':form
    }
    return render(request,'edit.html',context)

def delete(request,id):
        obj = Employee.objects.get(id=id)
        obj.delete()
        return redirect('login')

def user_login(request):
  pass