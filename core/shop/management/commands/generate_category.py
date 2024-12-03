from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
from shop.models import ProductCategoryModel

class Command(BaseCommand):
    help = 'Generate 10 fake product categories'

    def handle(self, *args, **kwargs):
        fake = Faker(locale="fa_IR")

        for _ in range(10):
            title = fake.word().capitalize()
            slug = slugify(title, allow_unicode=True)

            # Create and save the category
            ProductCategoryModel.objects.create(title=title, slug=slug)

        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake categories!'))
