from django.contrib import admin, messages
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
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    list_filter = ["membership"]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ["clear_inventory"]
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
    autocomplete_fields = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "LOW"
        return "FULL"

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

    @admin.action(description="Clear Inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f"{updated_count} Product were cleared")


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]
    search_fields = ["title"]

    @admin.display(ordering="-product_count")
    def product_count(self, collection):
        return collection.product_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("product"))

    # product_count.short_description = "Products"


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    min_num = 1
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    inlines = [OrderItemInline]
    list_display = ["payment_status", "customer"]
    # adding an instance of inline class


# making an inline class for orderItem inside order page
