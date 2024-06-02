from django.core.management.base import BaseCommand
from authentication.models import MedicineProblem
from faker import Faker
import random
from authentication.models import MyUser
from medicine.models import Medicine

class Command(BaseCommand):
    help = 'Inserts fake user data into the Medicine model'

    def add_arguments(self, parser):
        parser.add_argument('number_of_records', type=int, help='Number of fake records to insert')

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_records = kwargs['number_of_records']

        users = MyUser.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('no users found. please insert users first.'))
            return

        medicines = Medicine.objects.all()
        if not medicines.exists():
            self.stdout.write(self.style.ERROR('no medicine found. please insert medicines first.'))
            return

        for _ in range(number_of_records):
            medicine_problem = MedicineProblem(
                user = random.choice(users),
                medicine = random.choice(medicines)
            )

            medicine_problem.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully inserted {number_of_records} fake records into the medicine_problem model'))

