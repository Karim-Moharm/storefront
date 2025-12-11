from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>/", views.product_details),
    path("collection/<id>/", views.collection_details),
    path("collections/", views.collection_list),
]
