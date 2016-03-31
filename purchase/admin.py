from django.contrib import admin

# Register your models here.

from purchase.models import Purchase, Product


class PurchaseAdmin(admin.ModelAdmin):
	list_display = ('number', 'status', 'body')
	search_fields = ('number', 'status', 'body')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	search_fields = ('name', 'price')

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Product, ProductAdmin)
