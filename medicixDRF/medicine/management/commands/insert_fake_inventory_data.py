from django.core.management.base import BaseCommand
from medicine.models import Medicine, Inventory
from branch.models import Branch
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake inventory data'

    def add_arguments(self, parser):
        parser.add_argument('total_inventory', type=int, help="Indicates the number of fake inventory to create")

    def handle(self, *args, **kwargs):
        fake = Faker()
        total_inventory = kwargs['total_inventory']

        all_medicines = list(Medicine.objects.all())
        all_branches = list(Branch.objects.all())

        for medicine in all_medicines:
            for branch in all_branches:
                quantity = random.randint(1, 100)
                sold = random.randint(0, quantity)
                inventory = Inventory.objects.create(
                    medicine = medicine,
                    branch = branch,
                    quantity = quantity,
                    soled = sold,
                    expire_date = fake.date_between(start_date='today', end_date='+2y')
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total_inventory} fake inventory records.'))
