from django.urls import path
from django.conf.urls import url
from .import views
app_name = 'Employee'
urlpatterns=[
    url('dashbord',views.dash_Bord ,name= 'dashbord'),
    path('index',views.index,name='index'),
    path('register',views.add_Employee,name='regsiter'),
    path('changepass',views.changePassw,name='changepass'),
    path('show',views.updateinfo,name='show_data'),
    # path('edit/', views.employeeEdit, name='edit_emp'),
    # path('delete/<int:id>/', views.employeeDelete, name='del_emp'),
    path('edit/<int:id>/', views.edit, name='emp_edit'),
    path('delete/<int:id>/',views.delete, name='emp_delete'),
    path('emp_download',views.download, name='emp_download'),
    path('userlog/', views.index),

]

