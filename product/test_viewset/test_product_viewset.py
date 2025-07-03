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
from unicodedata import category


class TestProductViewSet(APITestCase):
    client=APIClient()

    def setUp(self):
        self.user=UserFactory()
        self.product=ProductFactory(title="pro controler",price=200.00)

    def test_get_all_product(self):
        response=self.client.get(reverse("product-list"kwargs={"version":"v1"}))
        self.assertEqual(responses.status_code,status.HTTP_200_OK)
        product_data=jason.loads(response.content)

        order=jason.loads(response.content)[0]
        self.assertEqual(product_data["product"][0]["title"],self.product.title)
        self.assertEqual(product_data["product"][0]["price"], self.product.price)
        self.assertEqual(product_data["product"][0]["active"], self.product.active)


    def test_create_product(self):
        category=CategoryFactory()
        data=jason.dumps({"title":"notbook","price":800,"category":[category.id]})
        data=jason.dumps({"product_id":[product.id],"user":user.id})

        response=self.client.post(
            reverse("product-list",kwargs={"version":"v1"}),
            data=data,
            content_type="apliccation/jason"
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        created_product=Product.obejects.get("notbook")
        self.assertEqual(create_product.title,"notbook")
        self.assertEqual(create_product.price, 800.00)


