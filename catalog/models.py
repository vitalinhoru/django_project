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
    title = models.CharField(max_length=100, verbose_name='наименование', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за штуку', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    update_date = models.DateTimeField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('-create_date',)


class Version(models.Model):
    title = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')
