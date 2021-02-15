from django.contrib import admin

from products.models import Product, Category, ProductCategory


class ProductCategoryInline(admin.TabularInline):
    """Описание полей модели ProductCategory для сайта администрирования."""

    model = ProductCategory
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    """Описание полей модели Product для сайта администрирования."""

    model = Product
    list_display = ('pk', 'title', 'published', 'deleted')
    list_filter = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    """Описание полей модели Category для сайта администрирования."""

    model = Category
    list_display = ('pk', 'title')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
