from django.urls import path
from . import views

# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import OrderViewSet, ProductViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register("orderview", OrderViewSet, basename="orders")
router.register("productview", ProductViewSet, basename="products")  # parent router

# netsted router ->  /domains/{domain_pk}/nameservers/{pk}
# for us ->     /productview/product_id/reviews/review_id
products_router = routers.NestedDefaultRouter(
    router, "productview", lookup="product"
)  # parent nested router
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

urlpatterns = (
    [
        path("products/", views.ProductList.as_view()),
        path("products/<int:id>/", views.ProductDetails.as_view()),
        path("collection/<id>/", views.collection_details),
        path("collections/", views.collection_list),
        path("productgen/", views.ProductListGen.as_view()),
        path("collgen/", views.CollectionListGen.as_view()),
        path("colldetgen/<int:pk>/", views.CollectionDetailsGen.as_view()),
        path("prodetgen/<int:pk>/", views.ProductDetailsGen.as_view()),
    ]
    + router.urls
    + products_router.urls
)
