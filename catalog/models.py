from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Наименование',
        help_text='Введите наименование'
    )   # наименование,
    description = models.CharField(
        max_length=200,
        verbose_name='Описание',
        help_text='Введите описание'
    )  # описание,

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование'
    )  # наименование,
    description = models.CharField(
        max_length=100,
        verbose_name='Описание',
        help_text='Введите описание'
    )  # описание,
    image = models.ImageField(
        upload_to='Product/photo',
        blank=True, null=True,
        verbose_name='Фото',
        help_text='Загрузите фото'
    )  # изображение
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию',
        null=True,
        blank=True,
        related_name='products'
    )  # категория,
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Цена',
        help_text='Введите цену продукта'
    )
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата создания',
        help_text='Укажите дату создания',
        auto_now_add=True
    )  # дата создания,
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата последнего изменения',
        help_text='Дата последнего изменения',
        auto_now=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Поставщик",
        help_text="Укажите поставщика товара",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    views_counter = models.PositiveIntegerField(
        default=0
    )
    is_publish = models.BooleanField(
        default=False,
        verbose_name="Опубликовать продукт?")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['description', 'category', 'price', 'created_at', 'updated_at', 'owner']
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
        ]

    def __str__(self):
        return self.name
