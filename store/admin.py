from django.contrib import admin
from django.db.models import Count
from . import models
from django.utils.html import format_html
from django.urls import reverse


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
        "promotion_count",
    ]

    list_display_links = ["title", "collection_title"]

    list_select_related = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "LOW"
        return "FILL"

    def collection_title(self, product):
        #  reverse(admin:appname_change)
        url = reverse(f"admin:store_collection_change", args=[product.collection.id])
        return format_html(
            "<a href='{}'>{}</a>",
            url,
            product.collection.title,
        )

    def promotion_count(self, product):
        return product.promotion_count

    def get_queryset(self, request):
        return (
            super().get_queryset(request).annotate(promotion_count=Count("promotions"))
        )

    """another method with one function
    def promotion_count(self, product):
        product.promotions.count()
    """


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]

    @admin.display(ordering="-product_count")
    def product_count(self, collection):
        return collection.product_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("product"))

    # product_count.short_description = "Products"
