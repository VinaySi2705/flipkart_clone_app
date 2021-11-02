from django.shortcuts import render
from clone.models import Product
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
# from django.http import HttpResponse


def dashboard(request):
    return render(request, "clone/dashboard.html")


def categories(request):
    products = Product.objects.all()
    return render(request, 'clone/categories.html', {'products': products})


def products(request):
    products = Product.objects.all()
    return render(request, 'clone/products.html', {'products': products})


def homepage(request):
    return render(request, 'clone/homepage.html')

# class LockedView(LoginRequiredMixin):
#     login_url = "admin:login"

# class Secr(LockedView):
#     def products(request):
#         if request.user.is_authenticated:
#             products = Product.objects.all()
#             return render(request, 'clone/products.html', {'products': products})
#         else:
#             return HttpResponse("Please login again")
#
#     def home(request):
#         if request.user.is_authenticated:
#             return render(request, 'clone/homepage.html')
#         else:
#             return HttpResponse("Please login again")

    # def categories(request):
    #     if request.user.is_authenticated:
    #         products = Product.objects.all()
    #         return render(request, 'clone/categories.html', {'products': products})
    #     else:
    #         return HttpResponse("Please login again")
