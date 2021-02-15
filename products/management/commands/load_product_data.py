import csv

from django.core.management.base import BaseCommand

from products.models import Product, Category, ProductCategory


class Command(BaseCommand):
    help = 'Load product data to database'

    def handle(self, *args, **options):
        """
        Функция при первом развертывании добавляет в базу продукты и категории
        (первая буква названия продукта)
        python manage.py load_product_data
        """

        with open('products/fixtures/products.csv') as isfile:
            reader = csv.reader(isfile)
            for row in reader:
                product_title, category_title = row
                category = Category.objects.get_or_create(title=category_title)
                product = Product.objects.get_or_create(title=product_title)
                ProductCategory.objects.get_or_create(category_id=category[0].id, product_id=product[0].id)


