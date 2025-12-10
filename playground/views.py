from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer
from store.models import Promotion
from django.db.models import Value, F, Func


# Create your views here.


def sayHello(request):
    # return query_set
    # output = Promotion.objects.all()
    # return object
    promotions = Promotion.objects.filter(discount__range=(10, 20))
    promtions_con = Promotion.objects.filter(description__icontains="Soft")

    # annotate -> create new colume (temp one) in database, which is full_name
    # FUNC -> use database functions like CONCAT, UPPER, LOWER
    # F -> get the field from database (select first_name from Customer)
    # Value -> when you want to add static text like ' ' (space)
    # function -> name of SQL Function u need to use
    queryset = Customer.objects.annotate(
        full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    )

    return render(
        request,
        "hello.html",
        {"user": "admin", "customer_name": queryset},
    )
