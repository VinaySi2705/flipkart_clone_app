from django.views import View
from clone.models import Category, Product
from django.shortcuts import redirect, render
from django.contrib import messages

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        item=Product.objects.get(id=product)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    if quantity<item.quantity:
                        cart[product]=quantity+1
                    else:
                        messages.warning(request,'Item is out of limit')
                        return redirect('homepage')
            else:
                if quantity<item.quantity:
                    cart[product]=1
                else:
                    messages.warning(request,'Item is out of limit')
                    return redirect('homepage')

        else:
            cart = {}
            if item.quantity!=0:
                cart[product]=1
            else:
                messages.warning(request,'Item is out of limit')
                return redirect('homepage')
        request.session['cart'] = cart
        # print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        # print('you are:', request.session.get('customer'))
        # print('email=>',request.session.get('email'))
        return render(request, 'index.html', data)
