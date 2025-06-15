from django.db import  models


class Order(models.Model):
    product=models.ManyToManyField(Product,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)