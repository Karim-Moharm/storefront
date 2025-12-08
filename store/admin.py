from django.contrib import admin
from .models import Product, Promotion, Collection

# Register your models here.

admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Collection)
