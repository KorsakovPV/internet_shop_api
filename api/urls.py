from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, CategoryViewSet

router_v1 = DefaultRouter()
router_v1.register('category', CategoryViewSet)
router_v1.register('product', ProductViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
