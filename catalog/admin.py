from django.contrib import admin
from catalog.models import Category, Product, Version
from users.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'version_number')


# class UserAdmin(admin.ModelAdmin):
#     list_filter = ('groups',)  # Добавляем фильтр по полю 'groups'
#
#
# admin.site.register(User)
#
#
# # @admin.register(User)
# # class UserAdmin(admin.ModelAdmin):
# #     list_display = ('first_name', 'last_name', 'is_verified')
