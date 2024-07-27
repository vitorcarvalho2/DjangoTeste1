from django.db import models

class Product(models.Model):
    name = models.CharField('Product_Name', max_length=100)
    price = models.DecimalField('Product_Price', decimal_places=2,max_digits=8)
    quantity = models.IntegerField('Product_Quantity')
    def __str__(self):
        return f'{self.name} '

class Client(models.Model):
    name = models.CharField('Client_name', max_length=30)
    surname = models.CharField('Client_surname', max_length=100)
    email = models.CharField('Client_email', max_length=100)
    def __str__(self):
        return f'{self.name} {self.surname}'

