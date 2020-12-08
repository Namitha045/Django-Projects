from rest_framework import serializers
from apiapp.models import Employee, Office, Department


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ('id','url', 'city','country', 'address')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id','url', 'name', 'superdepartment')
    

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('first', 'last', 'id', 'manager', 'department', 'office')



