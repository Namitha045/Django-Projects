##################################################################################################################
#!/usr/bin/env python3#
#Created by Namitha045#
#Date - 07 Dec 2020
# This script is used to load the django database with employee, office and department data
##################################################################################################################


import json
import urllib.request

from django.core.management import BaseCommand

from apiapp.models import Employee, Office, Department

service_url = 'https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees'

url = urllib.request.urlopen(service_url)
print('Retrieving Data.....!')
data = url.read().decode()
office_filename = os.path.join(BASEDIR, 'offices.json')
department_filename = os.path.join(BASEDIR, 'department.json')

try:
    js = json.loads(data)
except:
    js = None

with open(office_filename) as f:
    offices = json.load(f)
with open(department_filename) as d:
    departments = json.load(d)


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the Emp data,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    help = "Loads data from employee api into Database."

    def handle(self, *args, **options):
        if Employee.objects.exists() or Department.objects.exists() or Office.objects.exists():
            print("Employee data already loaded")
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print('Creating employee data')
        for row in offices:
            office = Office()
            office.id = row['id']
            office.city = row['city']
            office.country = row['country']
            office.address = row['address']
            office.save()
        for row in departments:
            department = Department()
            department.name = row['name']
            department.save()
            superdept = row['superdepartment']
            if superdept:
                supdep = Department.objects.get(id = superdept)
            else:
                supdep = None
            department.superdepartment = supdep
            department.save()
        for row in range(len(js)):
            employee = Employee()
            employee.first = js[row]['first']
            employee.last = js[row]['last']
            employee.id = js[row]['id']
            employee.save()
            mangr = js[row]['manager']
            if mangr:
                mngr_id = Employee.objects.get(id = mangr)
            else:
                mngr_id = None
            employee.manager = mngr_id
            dept = js[row]['department']
            if dept:
                dept_id = Department.objects.get(id = dept)
            else:
                dept_id = None
            employee.department = dept_id
            off = js[row]['office']
            if off: 
                off_id = Office.objects.get(id = off)
            else:
                off_id = None
            employee.office = off_id
            employee.save()

            
            
