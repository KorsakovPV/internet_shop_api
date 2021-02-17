from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """Класс сериализатор категории."""

    class Meta:
        """Мета класс. Определяем модель и поля модели."""

        fields = '__all__'
        model = Category


class ProductReadSerializer(serializers.ModelSerializer):
    """Класс сериализатор продуктов чтение."""

    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        """Мета класс. Определяем модель и поля модели."""

        fields = '__all__'  # ('title', 'published', 'deleted')
        model = Product


class ProductWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='title', many=True)

    class Meta:
        """Мета класс. Определяем модель и поля модели."""

        fields = '__all__'  # ('title', 'published', 'deleted')
        model = Product

    def validate(self, data):
        if len(data.get('category')) < 2:
            raise serializers.ValidationError(
                'У товара не может быть меньше 2 групп.')
        if len(data.get('category')) > 10:
            raise serializers.ValidationError(
                'У товара не может быть больше 10 групп.')
        return data
