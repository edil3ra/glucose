from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
from zipfile import ZipFile
from io import TextIOWrapper
from api.models import Glucose
from django.contrib.auth import get_user_model
import csv

FILENAME_SAMPLE = 'sample-data.zip'

class Command(BaseCommand):
    help = 'load csv to glucose'

    def handle(self, *args, **options):
        misc_folder = settings.BASE_DIR / 'misc'
        with ZipFile(misc_folder / FILENAME_SAMPLE) as zip:
            for filename in zip.namelist():
                with TextIOWrapper(zip.open(filename), encoding="utf-8") as file_zip:
                    name = file_zip.name.split('.')[0]
                    User = get_user_model()
                    user = User.objects.create_user(name)
                    rows = csv.reader(file_zip)
                    next(rows, None)
                    is_empty = next(rows,None)
                    if is_empty:
                        next(rows, None)
                    for row in rows:
                        device = row[0]
                        serie = row[1]
                        timestamp = row[2]
                        glucose = Glucose(device=device, serie=serie, timestamp=timestamp, user=user)
                        glucose.save()

        
