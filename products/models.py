"""Модели приложения Products."""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    """Модель для хранения категорий."""

    title = models.CharField(max_length=255,
                             unique=True,
                             verbose_name='Название категории')

    def __str__(self):
        """Переопределяет строковое представление объекта Category."""
        return f'{self.pk} - {self.title}'


class Product(models.Model):
    """Модель для хранения наименований товаров."""

    title = models.CharField(max_length=255,
                             verbose_name='Название товара')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    category = models.ManyToManyField(Category,
                                      through='ProductCategory',
                                      verbose_name='Категория')
    # category_count = models.IntegerField(
    #     validators=[MinValueValidator(1), MaxValueValidator(10)],
    #     verbose_name='Счетчик категорий')


    def __str__(self):
        """Переопределяем строковое представление модели Product."""
        return self.title


class ProductCategory(models.Model):
    """Модель для хранения отношения Товар-Категория."""

    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                related_name='product_category_related')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='product_category_related')
