"""
URL configuration for Lazapee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_employees, name='view_employees'),
    path('view_employee/', views.view_employees, name='view_employees'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('create_employee/<int:pk>/', views.create_employee, name='create_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('payroll/', views.payroll, name='payroll'),
    path('view_payslip/<int:pk>/', views.view_payslip, name='view_payslip'),
    path('delete_payslip/<int:pk>/', views.delete_payslip, name='delete_payslip'),
    path('get_payslips/', views.get_payslips, name='get_payslips'),
    path('get_analytics/', views.get_analytics, name='get_analytics')
]
