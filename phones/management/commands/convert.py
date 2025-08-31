# import os
from django.core.management.base import BaseCommand
# from django.conf import settings
from phones.models import Phone
from django.utils.text import slugify
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        fl = 'phones.csv'
        with open(fl,'r') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=';')
            con = 0
            for row in csv_reader:
                if con==0:
                    pass
                else:
                    print(row,'####################')
                    Phone.objects.create(id=row[0],name=row[1],price=row[3],image=row[2],release_data=row[4],lte_exists=row[5],slug=slugify(row[1]))
                con+=1
       