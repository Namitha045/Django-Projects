#from rest_framework.exceptions import ValidationError
#from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from rest_framework import viewsets, mixins

from apiapp.serializers import EmployeeSerializer, OfficeSerializer, DepartmentSerializer
from apiapp.models import Employee, Office, Department

class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('id',)
    search_fields = ('first', 'department',)
    pagination_class = ProductPagination

class OfficeList(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class DepartmentList(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = ProductPagination



    

    