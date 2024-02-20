from django.contrib import admin
from .models import *

class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

class Meta:
    model = Order

admin.site.register(Order, OrderAdmin)



class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

class Meta:
    model = Status

admin.site.register(Status, StatusAdmin)



class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

class Meta:
    model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)

