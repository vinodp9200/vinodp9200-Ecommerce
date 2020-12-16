from django.urls import path
from .import views

urlpatterns=[

    path('payslip',views.emp_Payslip),
    path('download',views.export_csv),
    path('pdf',views.export_pdf),


]