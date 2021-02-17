from django.shortcuts import render
from rest_framework import filters, status, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers import ProductReadSerializer, CategorySerializer, \
    ProductWriteSerializer
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
    # serializer_class = ProductReadSerializer

    def get_serializer_class(self):
        """Возвращает класс, который должен использоваться для сериализатора."""
        if self.action in ('list', 'retrieve'):
            return ProductReadSerializer
        return ProductWriteSerializer


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
        elif request.GET.get('price_min') or request.GET.get('price_max'):
            queryset = Product.objects.all()
            price_min = request.GET.get('price_min')
            if price_min:
                queryset = queryset.filter(price__gte=price_min)
            price_max = request.GET.get('price_max')
            if price_max:
                queryset = queryset.filter(price__lte=price_max)
        elif request.GET.get('is_published'):
            is_published = bool(request.GET.get('is_published'))
            queryset = Product.objects.filter(published=is_published)
        elif request.GET.get('is_deleted'):
            is_deleted = bool(request.GET.get('is_deleted'))
            queryset = Product.objects.filter(deleted=is_deleted)
        else:
            queryset = Product.objects.all()
        serializer = ProductReadSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = ProductWriteSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Product, id=kwargs['pk'])
        instance.deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)
    #
    # def perform_update(self, serializer):
    #     serializer.save()
    #
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)