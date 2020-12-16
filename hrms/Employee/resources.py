from import_export import resources
from .models import Employee

class PersonResource(resources.ModelResource):
    class Meta:
        model = Employee
