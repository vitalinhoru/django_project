from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, image_view
from django.conf import settings
from django.conf.urls.static import static

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),

    path('', image_view, name='image_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
