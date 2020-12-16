from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns=[

    url('leave', views.emp_Leave,name='leave'),
    path('logout', views.emp_Logout),

]