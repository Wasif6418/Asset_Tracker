from django.urls import path

from CorporateAssets import views
from .views import Asset_DetailView, AssetDetailView, EmployeeDetailView, CompanyDetailView



urlpatterns = [
    path('assetdetail/<slug:slug>/',  Asset_DetailView.as_view()),
    path('asset/<slug:slug>/', AssetDetailView.as_view()),
    path('employee/<slug:slug>/', EmployeeDetailView.as_view()),
    path('company/<slug:slug>/', CompanyDetailView.as_view())
]