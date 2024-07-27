from django.contrib import admin

from .models import Product, Client

class Adm_product(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Product,Adm_product)

class Adm_client(admin.ModelAdmin):
    list_display = ('name','surname','email')

admin.site.register(Client,Adm_client)
