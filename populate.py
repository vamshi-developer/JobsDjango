import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
import django
django.setup()

from testapp.models import HydJobs
from faker import Faker
faker=Faker()
from random import *
def phonenumber():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=faker.date()
        fcompany=faker.company()
        ftitle=faker.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility=faker.random_element(elements=('b.Tech',"m.Tech",'MCA','Mahes sir Student'))
        faddress=faker.address()
        fphonenumber=phonenumber()
        femail = faker.email()
        hyd_jobs_records=HydJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber
        )
n=int(input("Enter number of Records"))
populate(n)
print(f'{n} Records Inserted Successfully........!')