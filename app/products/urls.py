from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.products, name='get_products'),
    path('bulk_insert/', views.bulk_insert, name='bulk_insert'),
]
