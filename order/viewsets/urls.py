from os.path import basename

from django.urls import path ,include
from rest_framework import routes

from order import viewsets

from trabalho.trabalho.urls import urlpatterns

r=routers.SimpleRouter()
r.register(r"order",viewsets.OrderViewSet,basename="order")

urlpatterns=[
    path("",include(r.urls)),
]
