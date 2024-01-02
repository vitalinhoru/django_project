from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'title': 'Бакалея', 'description': 'Крупы'},
            {'title': 'Алкоголь', 'description': 'пиво, водка'},
            {'title': 'Мясо', 'description': 'говядина, свинина'},
            {'title': 'Химия', 'description': 'средство для чистки унитаза'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'title': 'Пиво', 'price': 70, 'description': '2.5 %', 'category': category_for_create[1]},
            {'title': 'Макароны', 'price': 100, 'description': 'твердый сорт', 'category': category_for_create[0]},
            {'title': 'Курица', 'price': 70, 'description': 'Азербайджанские', 'category': category_for_create[2]},
            {'title': 'Доместос', 'price': 100, 'description': 'птичье молоко', 'category': category_for_create[3]},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)



