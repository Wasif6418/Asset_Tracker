from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'company_id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'company_id']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'employee_id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'description', 'employee_id']


@admin.register(Asset_details)
class Asset_detailAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'checked_out_date', 'checked_in_date', 'condition_on_checkout', 'employee_id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'employee_id', 'asset_id']
