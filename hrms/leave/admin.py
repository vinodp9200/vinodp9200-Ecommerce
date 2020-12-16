from django.contrib import admin
from .models import emp_Leave
# Register your models here.

class Leave_Admin(admin.ModelAdmin):
    list_display = ['Date','Name','Employee_Code','Email','Address',
                    'Application_Type','From','To','Department']
    list_filter = ["Name"]
    search_fields = ['Employee_Code',"Name"]
    # title = ['name','code','mobile','address','gender','email','blood_group','department',
    #                 'designation','laptop','salary']

admin.site.register(emp_Leave,Leave_Admin)