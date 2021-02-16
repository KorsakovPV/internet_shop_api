from django.shortcuts import render
from rest_framework import filters, status, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        """
        Category list

        Возвращает группу по имени или пустой лис если группа не найдена или
        все группы если ключ category_title не указан.
        """
        try:
            category_title = request.GET['category_title']
            queryset = Category.objects.filter(title=category_title)
        except:
            queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def list(self, request, *args, **kwargs):
        """
        Product list

        Возвращает группу по имени или пустой лис если группа не найдена или
        все группы если ключ category_title не указан.
        """
        #TODO поправить докстринг
        if request.GET.get('product_title'):
            product_title = request.GET.get('product_title')
            queryset = Product.objects.filter(title=product_title)
        elif request.GET.get('category_id'):
            category_id = request.GET.get('category_id')
            category = get_object_or_404(Category, id=category_id)
            queryset = Product.objects.select_related().filter(category=category.id)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
