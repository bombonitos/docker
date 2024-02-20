from django.contrib import admin
from .models import *
from .models import Kitty
from .models import Orders


class UserAdmin (admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    list_filter = ('name',)
    search_fields = ['name', 'email']

class Meta:
    model = User

admin.site.register(User, UserAdmin)
admin.site.register(Kitty)
admin.site.register(Orders)



