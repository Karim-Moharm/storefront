from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ProductViewSet


router = DefaultRouter()

router.register("orderview", OrderViewSet, basename="orders")
router.register("productview", ProductViewSet, basename="products")


urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("products/<int:id>/", views.ProductDetails.as_view()),
    path("collection/<id>/", views.collection_details),
    path("collections/", views.collection_list),
    path("productgen/", views.ProductListGen.as_view()),
    path("collgen/", views.CollectionListGen.as_view()),
    path("colldetgen/<int:pk>/", views.CollectionDetailsGen.as_view()),
    path("prodetgen/<int:pk>/", views.ProductDetailsGen.as_view()),
] + router.urls
