from django.contrib.auth import get_user_model
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за штуку')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, null=True, verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('-create_date',)


class Version(models.Model):
    # title = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='название')
    title = models.CharField(max_length=100, verbose_name='наименование')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', default=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return f'{self.title}, {self.version_number}, {self.version_name}, {self.is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
