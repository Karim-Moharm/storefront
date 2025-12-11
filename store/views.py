from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
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


class ProductDetails(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)  # python dict
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(f"the product {serializer.data['title']} was update")

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        # check first if there is an order item for that product
        # we will use orderitem_set -> django create it automatically since the orderitem has a product foreign key
        if product.orderitem_set.count() > 0:
            return Response(
                {"error": "product can not be deleted as it associated with an order"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def collection_details(request, id):
    collection = get_object_or_404(Collection, pk=id)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def collection_list(request):
    if request.method == "GET":
        query_set = Collection.objects.all()
        serializer = CollectionSerializer(query_set, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            f"{serializer.data['title']} was created", status=status.HTTP_201_CREATED
        )
