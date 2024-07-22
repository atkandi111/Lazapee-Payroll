# Generated by Django 5.0.1 on 2024-04-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payroll_app", "0010_payslip_cycle_rate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payslip",
            name="net_pay",
        ),
        migrations.AlterField(
            model_name="employee",
            name="allowance",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="overtime_hours",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="overtime_pay",
            field=models.FloatField(default=0, null=True),
        ),
    ]
