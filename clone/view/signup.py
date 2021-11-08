from django.views import View
from django.shortcuts import render, redirect
from clone.models import Customer
from django.contrib.auth.hashers import make_password


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
