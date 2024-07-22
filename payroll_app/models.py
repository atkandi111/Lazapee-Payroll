from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from math import log, floor
import calendar
import pdb

class Employee(models.Model):
    name = models.CharField(max_length=25)
    id_number = models.IntegerField()
    rate = models.FloatField()
    overtime_hours = models.IntegerField(null=True, default=0)
    overtime_pay = models.FloatField(null=True, default=0)
    allowance = models.FloatField(null=True, default=0)

    def getName(self):
        return self.name

    def getID(self):
        return self.id_number

    def getRate(self):
        return self.rate

    def getOvertime(self):
        return self.overtime_pay

    def resetOvertime(self):
        self.overtime_pay = 0
        self.save()

    def getAllowance(self):
        return self.allowance

    def __str__(self):
        return f"pk: {self.id_number}, rate: {self.rate}"

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    rate = models.FloatField(default=0)
    cycle_rate = models.FloatField(default=0)
    overtime_pay = models.FloatField(null=True, default=0)
    allowance = models.FloatField(null=True, default=0)

    month = models.CharField(max_length=10)
    date_range = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    pay_cycle = models.IntegerField()

    tax = models.FloatField(null=True, default=0)
    philhealth = models.FloatField(null=True, default=0)
    pag_ibig = models.FloatField(null=True, default=0)
    sss = models.FloatField(null=True, default=0)
    total_deductions = models.FloatField(null=True, default=0)

    gross_pay = models.FloatField(null=True, default=0)
    total_pay = models.FloatField(null=True, default=0)
    total_pay_desc = models.CharField(max_length=300, default="")

    def getIDNumber(self):
        return self.id_number

    def getMonth(self):
        return self.month

    def getDateRange(self):
        return self.date_range

    def getYear(self):
        return self.year

    def getPayCycle(self):
        return self.pay_cycle

    def getRate(self):
        return self.rate

    def getCycleRate(self):
        return self.cycle_rate

    def getEarningsAllowance(self):
        return self.allowance

    def getDeductionsTax(self):
        return self.tax

    def getDeductionsHealth(self):
        return self.philhealth

    def getPagIbig(self):
        return self.pag_ibig

    def getSSS(self):
        return self.sss

    def getOvertime(self):
        return self.overtime_pay

    def getTotalPay(self):
        return self.total_pay

    def __str__(self):
        return f"pk: {self.pk}, Employee: {self.id_number}, Period: {self.month} {self.date_range}, {self.year}, Cycle: {self.pay_cycle}, Total Pay: {self.total_pay}"

@receiver(pre_save, sender=Employee)
def employee_pre_save(sender, instance, **kwargs):
    instance.overtime_pay = float(instance.rate) * float(instance.overtime_hours) * 1.5 / 160

@receiver(pre_save, sender=Payslip)
def payslip_pre_save(sender, instance, **kwargs):
    instance.id_number = instance.employee.id_number
    instance.rate = instance.employee.rate
    instance.cycle_rate = instance.rate / 2
    instance.overtime_pay = instance.employee.overtime_pay
    instance.allowance = instance.employee.allowance
    instance.gross_pay = instance.cycle_rate + instance.overtime_pay + instance.allowance

    if instance.pay_cycle == 1:
        date = "1-15"
        instance.date_range = "{} {}, {}".format(instance.month, date, instance.year)
        instance.pag_ibig = 100
        instance.tax = (instance.gross_pay - instance.pag_ibig) * 0.2
        instance.total_deductions = instance.pag_ibig + instance.tax
        
    if instance.pay_cycle == 2:
        for num, name in enumerate(calendar.month_name):
            if name == instance.month:
                month = num
                break

        year = int(instance.year)
        date = "16-{}".format(calendar.monthrange(year, month)[1])
        instance.date_range = "{} {}, {}".format(instance.month, date, instance.year)
        instance.philhealth = instance.rate * 0.04
        instance.sss = instance.rate * 0.045
        instance.tax = (instance.gross_pay - instance.philhealth - instance.sss) * 0.2
        instance.total_deductions = instance.philhealth + instance.sss + instance.tax

    instance.total_pay = instance.gross_pay - instance.total_deductions
    instance.total_pay_desc = int_to_en(int(instance.total_pay))

    # reset overtime hours
    instance.employee.overtime_hours = 0
    instance.employee.save()

def int_to_en(num):
    """
    taken from : https://stackoverflow.com/a/32640407
    """
    d = {   
            0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 
            5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 
            10 : 'Ten', 11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen', 
            15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen', 19 : 'Nineteen', 
            20 : 'Twenty', 30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
            70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' 
        }
    
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' Hundred'
        else: return d[num // 100] + ' Hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' Thousand'
        else: return int_to_en(num // k) + ' Thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' Million'
        else: return int_to_en(num // m) + ' Million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' Billion'
        else: return int_to_en(num // b) + ' Billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' Trillion'
    else: return int_to_en(num // t) + ' Trillion, ' + int_to_en(num % t)