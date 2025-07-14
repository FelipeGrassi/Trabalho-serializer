from http.client import responses
from importlib.resources import contents
from venv import create

import jason

from rest_framework import status
from rest_framework.test import APITestCase , APIClient

from django.urls import reverse
from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory,OrderFactory
from product.models import Product
from order.models import Order
from unicodedata import category

from trabalho.product.models import Category


class TestOrderViewSet(APITestCase):
    client=APIClient()

    def setUp(self):
        self.category=CategoryFactory(title="tec")
        self.product=ProductFactory(title="mouse",price=100,category=[self.category])
        self.order=OrderFactory(product=[self.product])

    def test_order(self):
        response=self.client.get(reverse("order-list"kwargs={"version":"v1"}))
        self.assertEqual(responses.status_code,status.HTTP_200_OK)

        self.asserEqual(response.status_code,status.HTTP_200_OK)

        import pdb;pdb.set_trace()

        order=jason.loads(response.content)[0]
        self.assertEqual(order_data["results"][0]["product"][0]["title"],self.product.title)
        self.assertEqual(order_data["results"][0]["product"][0]["price"], self.product.price)
        self.assertEqual(order_data["results"][0]["product"][0]["active"], self.product.active)
        self.assertEqual(order_data["results"][0]["product"][0]["category"][0]["title"], self.product.title)

    def test_create_order(self):
        user=UserFactory()
        product=ProductFactory()
        data=jason.dumps({"product_id":[product.id],"user":user.id})

        response=self.client.post(
            reverse("order-list",kwargs={"version":"v1"}),
            data=data,
            content_type="apliccation/jason"
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        created_order=Order.obejects.get(user=user)


