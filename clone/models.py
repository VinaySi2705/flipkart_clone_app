from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    items = models.CharField(max_length=50)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Products"
