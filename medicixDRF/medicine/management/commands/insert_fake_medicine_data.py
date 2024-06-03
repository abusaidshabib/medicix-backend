from django.core.management.base import BaseCommand
from medicine.models import Medicine
from branch.models import Branch
from faker import Faker
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generates fake medicine data'

    def add_arguments(self, parser):
        parser.add_argument('total_medicines', type=int, help='Indicates the number of fake medicines to create')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total_medicines = kwargs['total_medicines']

        categories = ["T","SY","SU","IN","TO","D","IN","L"]
        uses_for = ["H","A"]

        branches = Branch.objects.all()
        if not branches.exists():
            self.stdout.write(self.style.ERROR('No branches found. Please insert branches first.'))
            return

        for _ in range(total_medicines):
            medicine = Medicine(
                branch=random.choice(branches),
                brand = fake.company(),
                manufacturer = fake.company(),
                generic = fake.word(),
                strength = f"{random.randint(1,500)} mg",
                category = random.choice(categories),
                price = round(random.uniform(1, 100), 2),
                use_for = random.choice(uses_for),
                dar = fake.text(max_nb_chars=200),
                total = round(random.uniform(1,1000), 2),
                expire_date = fake.date_between(start_date='today',end_date='+2y')
            )
            medicine.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total_medicines} medicines'))

    # python manage.py insert_fake_medicine_data 100