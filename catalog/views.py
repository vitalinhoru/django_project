from django.shortcuts import render
from catalog.models import Product


def index(request):
    # return render(request, 'catalog/contacts.html')
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}: {message}')
    return render(request, 'catalog/contacts.html')

# def home(request):
#     return render(request, 'catalog/home.html')


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/product.html', context)