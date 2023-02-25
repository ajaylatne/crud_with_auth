from django.db import models


# Create your models here.
class Items(models.Model):
    order_no = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    address = models.CharField(max_length=20)
    email = models.EmailField()
    delivery_date = models.DateField()
