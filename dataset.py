import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Lazapee.settings")
import django
django.setup()

from payroll_app.models import Employee

dataset = [
    {'name': 'Emma Thompson', 'id_number': '738149', 'rate': 30246, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Michael Johnson', 'id_number': '509423', 'rate': 68423, 'allowance': 500.0, 'overtime': 0},
    {'name': 'Sophia Rodriguez', 'id_number': '169542', 'rate': 15783, 'allowance': 0.0, 'overtime': 0},
    {'name': 'James Wilson', 'id_number': '825736', 'rate': 80000, 'allowance': 250.0, 'overtime': 0},
    {'name': 'Olivia Martinez', 'id_number': '301974', 'rate': 44050, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Liam Garcia', 'id_number': '482619', 'rate': 57391, 'allowance': 750.0, 'overtime': 0},
    {'name': 'Ava Hernandez', 'id_number': '746812', 'rate': 9501, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Noah Smith', 'id_number': '398617', 'rate': 12035, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Isabella Johnson', 'id_number': '617294', 'rate': 48292, 'allowance': 0.0, 'overtime': 0},
    {'name': 'William Brown', 'id_number': '258731', 'rate': 35672, 'allowance': 500.0, 'overtime': 0},
    {'name': 'Sophia Miller', 'id_number': '947162', 'rate': 9988, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Oliver Davis', 'id_number': '503982', 'rate': 63219, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Charlotte Garcia', 'id_number': '174925', 'rate': 23784, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Liam Smith', 'id_number': '615249', 'rate': 49875, 'allowance': 1000.0, 'overtime': 0},
    {'name': 'Amelia Wilson', 'id_number': '932674', 'rate': 8721, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Ethan Johnson', 'id_number': '748125', 'rate': 30006, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Mia Brown', 'id_number': '365824', 'rate': 42095, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Lucas Martinez', 'id_number': '521049', 'rate': 86430, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Harper Wilson', 'id_number': '961347', 'rate': 19035, 'allowance': 250.0, 'overtime': 0},
    {'name': 'Alexander Taylor', 'id_number': '403719', 'rate': 58393, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Madison Garcia', 'id_number': '872403', 'rate': 23457, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Benjamin Hernandez', 'id_number': '615849', 'rate': 37026, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Evelyn Davis', 'id_number': '148693', 'rate': 50294, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Logan Smith', 'id_number': '792561', 'rate': 17825, 'allowance': 500.0, 'overtime': 0},
    {'name': 'Grace Anderson', 'id_number': '304852', 'rate': 62346, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Lucas Taylor', 'id_number': '631970', 'rate': 88235, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Layla Martinez', 'id_number': '478536', 'rate': 12930, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Henry Brown', 'id_number': '926571', 'rate': 46292, 'allowance': 750.0, 'overtime': 0},
    {'name': 'Chloe Martinez', 'id_number': '648921', 'rate': 23567, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Mason Johnson', 'id_number': '795612', 'rate': 52040, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Avery Davis', 'id_number': '210495', 'rate': 64729, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Mia Wilson', 'id_number': '876419', 'rate': 12671, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Sebastian Taylor', 'id_number': '342789', 'rate': 24035, 'allowance': 250.0, 'overtime': 0},
    {'name': 'Ella Rodriguez', 'id_number': '973251', 'rate': 54383, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Grayson Smith', 'id_number': '520817', 'rate': 13095, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Scarlett Garcia', 'id_number': '396874', 'rate': 89237, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Jackson Johnson', 'id_number': '618542', 'rate': 40729, 'allowance': 500.0, 'overtime': 0},
    {'name': 'Penelope Hernandez', 'id_number': '795142', 'rate': 64383, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Levi Martinez', 'id_number': '451920', 'rate': 28040, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Aria Wilson', 'id_number': '763195', 'rate': 8740, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Oliver Taylor', 'id_number': '590241', 'rate': 59024, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Hannah Brown', 'id_number': '318945', 'rate': 21099, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Mateo Garcia', 'id_number': '987321', 'rate': 39877, 'allowance': 250.0, 'overtime': 0},
    {'name': 'Ella Smith', 'id_number': '430612', 'rate': 19040, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Zoey Johnson', 'id_number': '184527', 'rate': 55029, 'allowance': 0.0, 'overtime': 0},
    {'name': 'David Martinez', 'id_number': '675249', 'rate': 49383, 'allowance': 500.0, 'overtime': 0},
    {'name': 'Victoria Davis', 'id_number': '291780', 'rate': 16050, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Daniel Hernandez', 'id_number': '530971', 'rate': 73017, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Nora Taylor', 'id_number': '467810', 'rate': 28764, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Carter Garcia', 'id_number': '872510', 'rate': 41099, 'allowance': 0.0, 'overtime': 0},
    {'name': 'Eleanor Smith', 'id_number': '205973', 'rate': 63050, 'allowance': 250.0, 'overtime': 0},
    {'name': 'John Wilson', 'id_number': '610243', 'rate': 52039, 'allowance': 0.0, 'overtime': 0}
]

# Employee.objects.all().delete()

for data in dataset:
    Employee.objects.create(
        name = data['name'], 
        id_number = data['id_number'], 
        rate = data['rate'], 
        overtime_hours = data['overtime'],
        allowance = data['allowance']
    )
