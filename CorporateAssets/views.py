from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import *
from CorporateAssets.serializers import *


class Asset_DetailView(APIView):
    def get(self, request, slug):
        asset_details= get_object_or_404(Asset_details, slug=slug.lower())  # filter by slug
        serializer = Asset_details(asset_details)
        return Response(serializer.data)

class AssetDetailView(APIView):
    def get(self, request, slug):
        asset = get_object_or_404(Asset, slug=slug.lower())  # filter by slug
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

class EmployeeDetailView(APIView):
    def get(self, request, slug):
        employee = get_object_or_404(Employee, slug=slug.lower())  # filter by slug
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class CompanyDetailView(APIView):
    def get(self, request, slug):
        company= get_object_or_404(Company, slug=slug.lower())  # filter by slug
        #brand = Brand.objects.filter(name__iexact=name).prefetch_related('categories__subcategories__products').first()
        serializer = CompanySerializer(company)
        return Response(serializer.data)



