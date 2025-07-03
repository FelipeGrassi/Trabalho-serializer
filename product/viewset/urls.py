from os.path import basename

from django.urls import path ,include
from rest_framework import routes

from product import viewsets

from trabalho.trabalho.urls import urlpatterns

r=routers.SimpleRouter()
r.register(r"product",viewsets.ProductViewSet,basename="product")
r.register(r"category",viewsets.ProductViewSet,basename="category")

urlpatterns=[
    path("",include(r.urls)),
]
