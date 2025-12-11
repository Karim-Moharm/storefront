from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("products/<int:id>/", views.ProductDetails.as_view()),
    path("collection/<id>/", views.collection_details),
    path("collections/", views.collection_list),
    path("productgen/", views.ProductListGen.as_view()),
    path("collgen/", views.CollectionListGen.as_view()),
    path("colldetgen/<int:pk>", views.CollectionDetailsGen.as_view()),
]
