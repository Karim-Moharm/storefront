from django.urls import path
from . import views

urlpatterns = [path("hello/", views.sayHello), path("gen_rel/", views.genRel)]
