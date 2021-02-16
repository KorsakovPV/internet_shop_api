from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """Класс сериализатор категории."""

    class Meta:
        """Мета класс. Определяем модель и поля модели."""

        fields = '__all__'
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    """Класс сериализатор продуктов."""

    category = CategorySerializer(many=True)

    # def validated_category(self):
    #     """Проверяем что колличестко категорий меньше 10"""

    class Meta:
        """Мета класс. Определяем модель и поля модели."""

        fields = '__all__'  #('title', 'published', 'deleted')
        model = Product
