import csv
import os

from django.core.management import BaseCommand

from test_botify.settings import BASE_DIR
from towns.models import Town


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_path = os.path.join(BASE_DIR, 'towns.csv')
        self.stdout.write('Importing towns')
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                _, created = Town.objects.get_or_create(
                    name=row['name'],
                    town_code=row['code'],
                    department_code=row['region_code'],
                    population=row['population'].replace(',', "")
                )
        self.stdout.write(self.style.SUCCESS('Towns imported successfully'))
