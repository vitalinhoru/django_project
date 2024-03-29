# Generated by Django 5.0 on 2024-01-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('preview_image', models.ImageField(upload_to='', verbose_name='превью')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='признак публикации')),
                ('views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
