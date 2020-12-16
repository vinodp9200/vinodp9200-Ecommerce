from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee
# Register your models here.
class EmployeeDataAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','code','mobile','address','gender','email','blood_group','department',
                    'designation','laptop','salary')
    list_filter = ("name",)
    search_fields = ("code",'mobile','name')
    # title = ['name','code','mobile','address','gender','email','blood_group','department',
    #                 'designation','laptop','salary']

admin.site.register(Employee, EmployeeDataAdmin)
