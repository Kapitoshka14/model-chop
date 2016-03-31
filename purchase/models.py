from django.db import models

class Product(models.Model):
  name = models.CharField('Название товара', max_length=50)
  price = models.FloatField('Стоимость', default=0.0)

class Purchase(models.Model):
  number = models.CharField('Номер покупки', max_length=50)
  price = models.FloatField('Цена', default=0.0)
  status=models.BooleanField('Проплачена ли', default=False)
  client = models.TextField('Данные о покупателе', default='Вася Пупкин, 8 912 345 67 89, Индекс ******, город ***, ул ***, дом ***, кв ***')
  body = models.TextField('Содержимое заказа')