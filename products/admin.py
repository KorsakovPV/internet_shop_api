from django.contrib import admin

from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Описание полей модели Product для сайта администрирования."""

    model = Product
    list_display = ('pk', 'title', 'category', 'published', 'deleted')
    list_filter = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    """Описание полей модели Category для сайта администрирования."""

    model = Category
    list_display = ('pk', 'title')





