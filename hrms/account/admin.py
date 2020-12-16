from django.contrib import admin
from  .models import Emp_Bank_Detail
# Register your models here.

class BankAdmin(admin.ModelAdmin):
     list_display = ('EName','Emp_Code','Bankname','Account_NO','IFSC_Code','Branch',
                     'Registerd_Mobile','GooglePayNo')
     list_filter = ['EName']
     search_fields = ['Emp_Code']

admin.site.register(Emp_Bank_Detail,BankAdmin)