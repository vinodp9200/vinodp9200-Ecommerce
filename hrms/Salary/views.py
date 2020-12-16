from django.shortcuts import render,redirect
from .models import Employee_Salary
from Employee.models import Employee
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template.loader import get_template
import csv
# Create your views here.

def export_csv(request):
    resopnce=HttpResponse(content_type='text/csv')
    resopnce['Content-Disposition']='attachment; filename=PaymentSlip.csv'
    writer=csv.writer(resopnce)
    writer.writerow(['Name', 'EMP_Code', 'Designatio', 'Department', 'Month_Year',
                     'Basic', 'H_R_A', 'Conc_All','Trans_All','CFA','PF_Employee',
                     'ESI_Employee','Loan_Advance','Tax','Total_deduction',
                     'Others','Medical_Allowance','Salary_Gross_PM','Telephone',
                     'Other','Salary'
                                                                                            'Designation', 'Laptop',
                     'salary'])
    emp = request.session.get('email')
    empdata = Employee_Salary.objects.all().filter(email=emp)
    for data in empdata:
        writer.writerow([data.Name, data.EMP_Code, data.Designatio, data.Department, data.Month_Year,
                         data.Basic, data.H_R_A, data.Conc_All,data.Trans_All,data.CFA,
                         data.PF_Employee,data.ESI_Employee,data.Loan_Advance,data.Tax,
                         data.Total_deduction,data.Others,data.Medical_Allowance,data.Salary_Gross_PM,
                         data.Telephone,data.Other,data.Salary])
    return resopnce

def export_pdf(request):
    # resopnce=HttpResponse(content_type='text/pdf')
    # resopnce['Content-Disposition']='attachment; filename=PaymentSlip.pdf'
    # resopnce['Content-Transfer-Encoading']='binary'
    # emp = request.session.get('email')
    # expenses = Employee_Salary.objects.all().filter(email=emp)
    # html_string=render_to_string(
    #     'expenses/payslip.html',{'expenses':expenses,'total':0}
    # )
    # html=HTML(string=html_string)
    # result=html.write_pdf()
    # return resopnce
    pass

def emp_Payslip(request):
    emp = request.session.get('email')
    slip=Employee_Salary.objects.all().filter(email=emp)
    context={'slip':slip}
    return render(request,'dashboard/payslip.html',context)




