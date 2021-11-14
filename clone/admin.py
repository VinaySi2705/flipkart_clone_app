from django.contrib import admin
from . models import Product, Category, Customer, Order
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price','quantity', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)
