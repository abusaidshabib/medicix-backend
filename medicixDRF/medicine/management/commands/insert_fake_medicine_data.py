from django.core.management.base import BaseCommand
from medicine.models import Medicine
from branch.models import Branch
from content.models import Subcategory
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

        subcategories = list(Subcategory.objects.all())
        if not subcategories:
            self.stdout.write(self.style.ERROR('No Subcategories found. Please insert Subcategories first.'))
            return

        for _ in range(total_medicines):
            medicine = Medicine(
                brand = fake.company(),
                manufacturer = fake.company(),
                generic = fake.word(),
                strength = f"{random.randint(1,500)} mg",
                subcategory = random.choice(subcategories),
                price = round(random.uniform(1, 100), 2),
                medicine_type = random.choice(categories),
                use_for = random.choice(uses_for),
                dar = fake.text(max_nb_chars=200),
            )
            medicine.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total_medicines} medicines'))

    # python manage.py insert_fake_medicine_data 100