from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('catalog/<int:pk>/', products_detail, name='products_detail')
]
