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

        with open('products/fixtures/products2.csv') as isfile:
            reader = csv.reader(isfile)
            category_dict = dict()
            for row in reader:
                product_title, price, category_title = row[0], row[1], row[2:]
                product = Product.objects.get_or_create(title=product_title, price=price)[0]
                # category_list = list()
                for item in category_title:
                    if item in category_dict.keys():
                        category = category_dict[item]
                    else:
                        category = Category.objects.get_or_create(title=item)[0]
                        category_dict[item] = category
                    # category_list.append(category)
                    ProductCategory.objects.get_or_create(category_id=category.id, product_id=product.id)


