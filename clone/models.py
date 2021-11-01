from django.db import models

# Create your models here.


class Product(models.Model):
    categories = models.CharField(max_length=50)
    items = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Products"
