from django.contrib import admin
from .models import Product, Promotion, Collection, Customer

# Register your models here.

admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Collection)
admin.site.register(Customer)
