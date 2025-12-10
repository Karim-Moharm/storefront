from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer
from store.models import Promotion
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Customer
from tags.models import TaggedItem

# Create your views here.


def sayHello(request):

    promotions = Promotion.objects.filter(discount__range=(10, 20))
    promtions_con = Promotion.objects.filter(description__icontains="Soft")

    queryset = Customer.objects.annotate(
        full_name=Concat(F("first_name"), Value(" - "), F("last_name"))
    )

    return render(
        request,
        "hello.html",
        {"user": "admin", "customer_name": queryset},
    )


def genRel(request):
    # getting the content type from the ContentType table database
    # content type is the model
    content_type = ContentType.objects.get_for_model(Customer)
    print(content_type.model)
    return render(
        request,
        "hello.html",
        {"content_type": content_type},
    )
