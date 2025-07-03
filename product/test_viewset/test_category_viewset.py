from http.client import responses
from importlib.resources import contents
from venv import create

import jason

from rest_framework import status
from rest_framework.test import APITestCase , APIClient

from django.urls import reverse
from product.factories import CategoryFactory

from product.models import Category
from unicodedata import category


class CategoryViewSet(APITestCase):
    client=APIClient()

    def setUp(self):
        self.category=CategoryFactory(title="books ")


    def test_get_all_category(self):
        response=self.client.get(reverse("category-list"kwargs={"version":"v1"}))
        self.assertEqual(responses.status_code,status.HTTP_200_OK)
        category_data=jason.loads(response.content)

        order=jason.loads(response.content)[0]
        self.assertEqual(category_data["product"][0]["title"],self.category.title)



    def test_create_category(self):

        data=jason.dumps({"title":"Tec"})
        data=jason.dumps({"product_id":[product.id],"user":user.id})

        response=self.client.post(
            reverse("category-list",kwargs={"version":"v1"}),
            data=data,
            content_type="apliccation/jason"
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        created_category=Category.obejects.get("Tec")
        self.assertEqual(created_category.title,"Tec")



