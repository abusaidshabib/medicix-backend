from django.core.management.base import BaseCommand
from content.models import MainCategory, Category, Subcategory
from faker import Faker
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generate fake medicine data'

    def add_arguments(self, parser):
        parser.add_argument('total_categories', type=int, help="Indicates the number of categories to create")

    def handle(self, *args, **kwargs):
        fake = Faker()
        total_categories = kwargs['total_categories']
        main_categories = []

        for _ in range(total_categories):
            main_category = MainCategory(
                name=fake.unique.word()
            )
            main_category.save()

            for _ in range(random.randrange(1, 5)):
                category = Category(
                    maincategory = main_category,
                    name=fake.unique.word()
                )
                category.save()

                for _ in range(random.randrange(1, 3)):
                    subcategory = Subcategory(
                        category=category,
                        name=fake.unique.word()
                    )
                    subcategory.save()
            self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))
