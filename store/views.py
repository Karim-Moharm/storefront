from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
from rest_framework import status


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        queryset = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(
            data=request.data
        )  # requets the data in serializer var
        serializer.is_valid(raise_exception=True)  # validate the data
        # saving the data in database
        serializer.save()
        return Response(
            f"the object with {serializer.data['id']} was created",
            status=status.HTTP_201_CREATED,
        )


@api_view(["GET", "PUT"])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)  # object
    if request.method == "GET":
        serializer = ProductSerializer(product)  # python dict
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(f"the product {serializer.data['title']} was update")


@api_view()
def collection_details(request, id):
    collection = get_object_or_404(Collection, pk=id)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)
