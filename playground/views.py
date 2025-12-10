from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection
from store.models import Promotion
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Customer
from tags.models import TaggedItem

# Create your views here.


def sayHello(request):

    # Collection.objects.create(title="Phones", featured_product_id=None)
    collection = Collection()
    collection.title = "Colthes"
    collection.featured_product_id = None
    collection.save()
    return render(
        request,
        "hello.html",
    )


def genRel(request):
    # getting the content type from the ContentType table database
    # content type is the model
    # this returns an object ---  <ContentType: store | customer>

    query_set = TaggedItem.objects.get_tags_for(Customer, 1)

    return render(
        request,
        "hello.html",
        {"result": list(query_set)},
    )
