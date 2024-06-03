# authentication/management/commands/insert_fake_user_data.py

from django.core.management.base import BaseCommand
from authentication.models import User  # Adjust the import according to your app name
from branch.models import Branch
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Inserts fake user data into the User model'

    def add_arguments(self, parser):
        parser.add_argument('number_of_records', type=int, help='Number of fake records to insert')

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_records = kwargs['number_of_records']

        # Ensure there are branches available to assign
        branches = Branch.objects.all()
        if not branches.exists():
            self.stdout.write(self.style.ERROR('No branches found. Please insert branches first.'))
            return

        for _ in range(number_of_records):
            user = User(
                branch=random.choice(branches),
                username=fake.user_name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                is_active=True,
                is_staff=fake.boolean(chance_of_getting_true=50),
                is_admin=fake.boolean(chance_of_getting_true=10),
                gender=random.choice(["M", "F", "T"])
            )

            user.set_password('1234')
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully inserted {number_of_records} fake records into the MyUser model'))

    # python manage.py insert_fake_user_data 100