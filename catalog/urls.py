from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, index, product


app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),
]
