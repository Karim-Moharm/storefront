from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from store.models import Promotion


# Create your views here.


def sayHello(request):
    # return query_set
    # output = Promotion.objects.all()
    # return object
    promotions = Promotion.objects.filter(discount__range=(10, 20))
    return render(request, "hello.html", {"user": "admin", "promotions": promotions})
