from django.contrib import admin
from .models import Product, Promotion, Collection, Customer

# Register your models here.

admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Collection)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "membership"]


admin.site.register(Customer, CustomerAdmin)
