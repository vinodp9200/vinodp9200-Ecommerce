from django.shortcuts import render,redirect,HttpResponse
from .forms import Emp_Bank_Detail
from django.contrib.auth.models import User
from .forms import EmpAccountForm,UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib import messages
# Create your views here.

def Account(request):
    form=EmpAccountForm(request.POST or None)
    if form.is_valid():
        messages.success(request,'Account Crated Successfully ')
        form.save()
        return redirect('/dashbord')
    context={'form':form}
    return render(request,'empaccount.html',context)

def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        messages.success(request,'Account Crated Successfully ')
        form.save()
        return redirect('/login')
    else:
        context={'form':form}
        return render(request,'adduser.html',context)



          # if user is not None:
          #     # if not user.is_active:
          #         login(request, user)
          #         print('activate')
          #         return redirect("/dashbord")
          #
          #     # else:
          #     #     # Return a 'disabled account' error message
          #     #     return redirect('/login')
          #
          # else:
          #     text='Now You are not activate by user'
          #     conetext={'data':text}
          #     return redirect('/login',conetext)



      # else:
      #     form = AuthenticationForm()
      #     context = {'form': form}
      #     # the login is a  GET request, so just show the user the login form.







