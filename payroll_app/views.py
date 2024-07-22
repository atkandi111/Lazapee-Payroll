from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import models
from .models import Employee, Payslip
from math import log

import pdb;

def view_employees(request):
    if request.method == "POST":
        pk = int(request.POST.get('pk'))
        hours = float(request.POST.get('overtime'))
        operation = request.POST.get('operation')

        if operation == 'minus':
            hours = -hours

        employee = Employee.objects.get(pk=pk)
        employee.overtime_hours = max(0, employee.overtime_hours + hours)
        employee.save()
        return JsonResponse({'overtime_pay': employee.overtime_pay})
    else:
        employee_objects = Employee.objects.all()
        return render(request, 'payroll_app/view_employees.html', {'employees':employee_objects})

def delete_employee(request, pk):
    Employee.objects.filter(pk=pk).delete()
    return redirect('view_employees')

def create_employee(request, pk=None):
    if request.method == "POST":
        name = request.POST.get('name')
        id_number = request.POST.get('id_number')
        rate = request.POST.get('rate')
        allowance = request.POST.get('allowance')

        errors = {}

        if not name or any(i.isdigit() for i in name):
            errors['name'] = 'Name should only contain letters.'

        if not id_number or any(i.isalpha() for i in id_number):
            errors['id_number'] = 'ID should only contain numbers.'

        if not rate or any(i.isalpha() for i in rate):
            errors['rate'] = 'Rate should only contain numbers.'

        if any(i.isalpha() for i in allowance):
            errors['allowance'] = 'Allowance should only contain numbers (if provided).'

        if not errors:
            employees = Employee.objects.filter(id_number=id_number)
            if isinstance(pk, int): # trying to update employee
                if employees.exists():
                    employees.update(name=name, id_number=id_number, rate=rate, allowance=allowance)
                    for employee in employees:
                        employee.save()
                    return JsonResponse({'success': True})
                else:
                    errors['id_number'] = 'Employee does not exist'

            else: # trying to create new employee
                if employees.exists():
                    errors['id_number'] = 'Employee ID already exists'
                else:
                    employees.create(name=name, id_number=id_number, rate=rate, overtime_hours=0, allowance=allowance)
                    return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': errors})
    
    else:
        if isinstance(pk, int):
            context = {'employee': Employee.objects.get(pk=pk)}
        else:
            context = {}

        return render(request, 'payroll_app/create_employee.html', context)
    
def payroll(request):
    if request.method == "POST":
        id_numbers = request.POST.getlist('id_numbers')
        month = request.POST.get('month')
        year = request.POST.get('year')
        cycle = int(request.POST.get('cycle'))

        employees = Employee.objects.filter(id_number__in=id_numbers)

        payslip_data = {
            'pk' : [],
            'id_number' : [],
            'date_range' : [],
            'net_pay' : [],
            'duplicate_count' : 0
        }
        # if employees.exists():

        for employee in employees:
            if Payslip.objects.filter(employee=employee, month=month, year=year, pay_cycle=cycle).exists():
                payslip_data['duplicate_count'] += 1
                continue

            payslip = Payslip.objects.create(employee=employee, month=month, year=year, pay_cycle=cycle)

            payslip_data['pk'].append(payslip.pk)
            payslip_data['id_number'].append(payslip.id_number)
            payslip_data['date_range'].append(payslip.date_range)
            payslip_data['net_pay'].append(payslip.total_pay)

        return JsonResponse(payslip_data)
    
    employee_objects = Employee.objects.all()
    payslip_objects = Payslip.objects.all().order_by('pk').reverse()

    return render(request, 'payroll_app/payroll.html', {'payslips':payslip_objects, 'employees':employee_objects})

def get_payslips(request):
    if request.method == "POST":
        if request.POST.get('all_time') == 'true':
            payslips = Payslip.objects.all().order_by('pk').reverse()

        else:
            month = request.POST.get('month')
            year = request.POST.get('year')

            payslips = Payslip.objects.filter(month=month, year=year).order_by('pk').reverse()

        payslip_data = {
            'pk'         : list(payslips.values_list('pk', flat=True)),
            'id_number'  : list(payslips.values_list('id_number', flat=True)),
            'date_range' : list(payslips.values_list('date_range', flat=True)),
            'cycle'      : list(payslips.values_list('pay_cycle', flat=True)),
            'total_pay'  : list(payslips.values_list('total_pay', flat=True))
        }

        return JsonResponse(payslip_data)

def get_analytics(request): # try caching
    if request.method == "POST": # GET
        payslips = None

        if request.POST.get('all_time') == 'true':
            payslips = Payslip.objects.all()
        else:
            month = request.POST.get('month')
            year = request.POST.get('year')

            payslips = Payslip.objects.filter(month=month, year=year)

        data = payslips.aggregate(
            total_gross_pay  = models.Sum('gross_pay'),
            total_deductions = models.Sum('total_deductions'),
            total_net_pay    = models.Sum('total_pay')
        )

        """
        modified from : https://stackoverflow.com/a/45478574
        """
        units = ['', 'K', 'M', 'B', 'T']
        for total, amount in data.items():
            amount = max(1, amount)
            magnitude = min(4, int(log(amount, 1000)))

            coefficient = amount / 1000 ** magnitude
            unit = units[magnitude]

            data[total] = "{:.2f}{}".format(coefficient, unit)

        data['length'] = payslips.count()
        return JsonResponse(data)
    
def view_payslip(request, pk):
    payslip = Payslip.objects.get(pk=pk)
    return render(request, 'payroll_app/view_payslip.html', {'payslip':payslip})

def delete_payslip(request, pk):
    Payslip.objects.filter(pk=pk).delete()
    return redirect('payroll')