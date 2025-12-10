from django.contrib import admin
from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "membership"]
    list_editable = ["membership", "last_name", "first_name"]
    list_per_page = 10
    # if you want to edit first_name you must add
    # list_display_link = ["field not in list_d=editable"]
    list_display_links = ["email"]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "price",
        "inventory_status",
        "collection_title",
    ]

    list_select_related = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "LOW"
        return "FILL"

    def collection_title(self, product):
        return product.collection.title


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]

    def product_count(self, collection):
        """
        product_set is the reverse FK, django automatically creats it
        returns all products that point to this collection
        """
        return collection.product_set.count()

    product_count.short_description = "Products"
