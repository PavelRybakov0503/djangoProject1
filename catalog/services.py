# from django.core.cache import cache
#
# from catalog.models import Product
# from config.settings import CACHE_ENABLED
#
# def get_products_from_cache():
#     """Получает данные по продуктам из кэша, если кэш пуст, получает данные из БД."""
#     if not CACHE_ENABLED:
#         return Product.get_objects.all()
#     key = "product_list"
#     products = cache.get(key)
#     if products is not None:
#         return products
#     products = Product.objects.all()
#     cache.set(key, products)
#     return products

from .models import Category, Product


class CategoryService:
    @staticmethod
    def get_all_categories():
        """
        Возвращает все категории
        """
        return Category.objects.all()

    @staticmethod
    def get_products_from_category(category):
        """
        Возвращает продукты из указанной категории
        """
        return Product.objects.filter(category=category)
