from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        # Удаляем все существующие продукты и категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем тестовые категории
        category1 = Category.objects.create(name='Электроника')
        category2 = Category.objects.create(name='Одежда')

        # Создаем тестовые продукты
        Product.objects.create(name='Смартфон', price=500.0, category=category1)
        Product.objects.create(name='Ноутбук', price=1000.0, category=category1)
        Product.objects.create(name='Футболка', price=20.0, category=category2)
        Product.objects.create(name='Джинсы', price=40.0, category=category2)

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены'))
