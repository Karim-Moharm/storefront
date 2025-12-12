from .views import cartViewSet, CartItemViewSet
from rest_framework_nested import routers
from django.urls import path, include


router = routers.DefaultRouter()


router.register("carts", cartViewSet, basename="carts")

# carts/<cart_id>/cartitem/<id>
cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("cartitem", CartItemViewSet, basename="cartitem")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(cart_router.urls)),
]
