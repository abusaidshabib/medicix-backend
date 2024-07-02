from django.core.management.base import BaseCommand
from branch.models import Branch, BranchAddress
from authentication.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Inserts fake branch data into the Branch model'

    def add_arguments(self, parser):
        parser.add_argument('number_of_records', type=int, help='Number of fake records to insert')

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_records = kwargs['number_of_records']
        user = User.objects.get(email="admin@gmail.com")

        for _ in range(number_of_records):
            last_branch = Branch.objects.order_by('-id').first()
            if not last_branch:
                branch_code = 'BR1'
            else:
                branch_code = f'BR{last_branch.id + 1}'
            # print(last_branch)
            branch = Branch(
                name = fake.company(),
                branch_code = branch_code,
                created_by = user,
            )
            branch.save()

            branch_address = BranchAddress(
                branch = branch,
                house_number = fake.building_number(),
                street_name = fake.street_name(),
                city = fake.city(),
                state = fake.state(),
                post_code = fake.zipcode(),
                country = fake.country()
            )
            branch_address.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully inserted {number_of_records} fake records into the Branch model'))

        # python manage.py insert_fake_branch_data 100