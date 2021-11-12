from django.shortcuts import render, redirect
from clone.models import Product
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        remove_item = request.POST.get('remove_item')
        clear = request.POST.get('clear')
        if remove_item:
            cart = request.session.get('cart')
            cart.pop(remove_item)
            request.session['cart'] = cart
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            return render(request, 'cart.html', {'products': products})

        elif clear:
            request.session.get('cart').clear()
            request.session['cart'] = {}
            return redirect('cart')
