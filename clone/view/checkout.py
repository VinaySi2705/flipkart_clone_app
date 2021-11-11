from django.views import View
from clone.models import Product, Order, Customer
from django.shortcuts import redirect, render


class Checkout(View):
    def get(self, request):
        return redirect('cart')

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        # if not customer:
        #     return redirect('login')
        cart = request.session.get('cart')
        if not cart:
            error_message = "Cart is empty!!please add item to the cart"
            return render(request, 'index.html', {'error': error_message})
        products = Product.get_products_by_id(list(cart.keys()))

        # print(address,phone,customer,cart,products)
        if address and phone:
            for product in products:
                order = Order(customer=Customer(id=customer),
                              product=product,
                              price=product.price,
                              address=address,
                              phone=phone,
                              quantity=cart.get(str(product.id)),
                              )
                order.save()

            request.session['cart'] = {}
            return redirect('cart')

        else:
            return redirect('cart')
