from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    """Описание полей модели Product для сайта администрирования."""

    model = Product
    list_display = ('pk', 'title', 'unit',)
    list_filter = ('title',)