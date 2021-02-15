"""Модели приложения Products."""
from django.db import models


class Category(models.Model):
    """Модель для хранения категорий."""

    title = models.CharField(max_length=255,
                             unique=True,
                             verbose_name='Название категории')
    # slug = models.SlugField(unique=True,
    #                         verbose_name='Слаг категории')

    def __str__(self):
        """Переопределяет строковое представление объекта Category."""
        return f'{self.pk} - {self.title} - {self.slug}'


class Product(models.Model):
    """Модель для хранения наименований товаров."""

    title = models.CharField(max_length=255,
                             verbose_name='Название товара')
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    category = models.ManyToManyField(Category,
                                      verbose_name='Категория',
                                      on_delete=models.PROTECT)

    def __str__(self):
        """Переопределяем строковое представление модели Product."""
        return self.title


# class ProductCategory(models.Model):
#     """Модель для хранения отношения Товар-Категория."""
#
#     product = models.ForeignKey(Product, on_delete=models.PROTECT,
#                                 related_name='product_category_related')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,
#                                  related_name='product_category_related')
