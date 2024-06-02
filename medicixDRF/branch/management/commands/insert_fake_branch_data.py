from django.core.management.base import BaseCommand
from branch.models import Branch
from faker import Faker

class Command(BaseCommand):
    help = 'Inserts fake branch data into the Branch model'

    def add_arguments(self, parser):
        parser.add_argument('number_of_records', type=int, help='Number of fake records to insert')

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_records = kwargs['number_of_records']

        for _ in range(number_of_records):
            branch = Branch(
                name = fake.company(),
                city = fake.city(),
                state = fake.state(),
                post_code = fake.zipcode()
            )
            branch.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully inserted {number_of_records} fake records into the Branch model'))

        # python manage.py insert_fake_branch_data 100000000