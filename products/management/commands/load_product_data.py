import csv

from django.core.management.base import BaseCommand

from products.models import Product, Category


class Command(BaseCommand):
    help = 'Load product data to database'

    def handle(self, *args, **options):
        """
        Функция при первом развертывании добавляет в базу продукты и категории
        (первая буква названия продукта)
        python manage.py load_product_data
        """

        with open('recipes/fixtures/ingredients.csv') as isfile:
            reader = csv.reader(isfile)
            for row in reader:
                title, category_title = row
                category = Category.objects.get_or_create(title=category_title)
                Product.objects.get_or_create(title=title, category=category)

