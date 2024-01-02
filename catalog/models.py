from django.db import models

class Product(models.Model):


    class Meta():
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):


    class Meta():
        verbose_name = 'каталог'
        verbose_name_plural = 'каталоги'
