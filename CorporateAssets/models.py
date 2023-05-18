from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import django_userforeignkey.models.fields

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


class Asset(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Asset_details(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    checked_out_date = models.DateTimeField()
    checked_in_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_checking = models.CharField(max_length=100, null=True, blank=True)

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

