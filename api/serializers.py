from rest_framework import serializers
from api.models import Company, Employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url','company_id','name', 'location', 'about', 'type','added_date', 'active']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url','id','name','email','address','mobile_number','about','position','company']
