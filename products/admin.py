from django.contrib import admin
from .models import *

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

class Meta:
    model = Product

admin.site.register(Product, ProductAdmin)



class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

class Meta:
    model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)



