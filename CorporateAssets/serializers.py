from rest_framework import serializers, generics

from .models import Company, Employee, Asset,Asset_details


class Asset_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset_details
        fields = ('id', 'name', 'slug', 'checked_out_date', 'checked_in_date', 'condition_on_checkout', 'condition_on_checking', 'employee_id', 'asset_id')
class AssetSerializer(serializers.ModelSerializer):
    asset_details= Asset_detailsSerializer(many=True, read_only=True)

    class Meta:
        model = Asset
        fields = ('id', 'name', 'slug', 'description',  'employee_id')
class EmployeeSerializer(serializers.ModelSerializer):
    asset= AssetSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'slug' 'company_id')

class CompanySerializer(serializers.ModelSerializer):
    employee= EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'slug')