from django.shortcuts import render
from clone.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.http import HttpResponse


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class Secr(LockedView):
    def all_products(request):
        if request.user.is_authenticated:
            products = Product.objects.all()
            return render(request, 'clone/products.html', {'products': products})
        else:
            return HttpResponse("Please login again")

    def home(request):
        if request.user.is_authenticated:
            return render(request, 'clone/base.html')
        else:
            return HttpResponse("Please login again")

    def categories(request):
        if request.user.is_authenticated:
            products = Product.objects.all()
            return render(request, 'clone/categories.html', {'products': products})
        else:
            return HttpResponse("Please login again")
