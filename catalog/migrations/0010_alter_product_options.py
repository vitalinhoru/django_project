# Generated by Django 4.2.4 on 2024-02-03 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-create_date',), 'permissions': [('set_published', 'Может публиковать'), ('change_product_description', 'Моет менять описание'), ('change_product_category', 'Может менять категорию продукта')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]