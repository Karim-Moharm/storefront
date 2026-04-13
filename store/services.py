from rest_framework.exceptions import ValidationError 

class StoreService:
    @staticmethod
    def delete_product(product):
        if product.inventory > 0:
            raise ValidationError({
                "inventory": "the inventory is not empty, you can't delete this product"
            })
        if product.orderitem_set.count() > 0:
            raise ValidationError({
                "Order Item": "the product have active order items, \
                    please remove them to be able to delete the product"
            })
        product.delete()

    @staticmethod
    def delete_collection(collection):
        if collection.product_set.count() > 0:
            raise ValidationError({
                "error": "you cant delete the collection because it has products"
            })
        collection.delete()
