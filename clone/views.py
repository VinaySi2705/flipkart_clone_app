from django.shortcuts import render, redirect
from clone.models import Product, Category, Customer, Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# Create your views here.


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        # print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        # print('you are:', request.session.get('email'))
        return render(request, 'index.html', data)


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # here we validate the input data
        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email,
                 }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password
                            )

        error_message = self.validateCustomer(customer)
        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()  # here we call the function from model customer
            return redirect('homepage')
        else:
            value['error'] = error_message
            return render(request, 'signup.html', value)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 char long or more"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last name must 4 or more char long"
        elif not customer.phone:
            error_message = "phone number required"
        elif len(customer.phone) < 10:
            error_message = "phone number must be of 10 digits"
        elif len(customer.password) < 6:
            error_message = "password must be of 6 char long"
        elif len(customer.email) < 5:
            error_message = "Email must be 5 char long"
        elif customer.is_exist():
            error_message = "Email Address already registered.."

        return error_message


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "Email or Password invalid!!!!"
        else:
            error_message = "Email or Passworrd is invalid!!"
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        if not customer:
            return redirect('login')

        # print(address,phone,customer,cart,products)
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


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})
