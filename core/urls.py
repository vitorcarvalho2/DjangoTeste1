from django1.urls import path

from .views import index, contact, product

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('product/<int:pk>', product, name="product"),
]

