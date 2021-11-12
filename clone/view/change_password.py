from django.shortcuts import render, redirect
from django.views import View
from clone.models import Customer
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages

class ChangePassword(View):
    def get(self, request):
        return render(request, 'change_password.html')

    def post(self, request):
        current_password = request.POST.get('current')
        new_password = request.POST.get('new')
        confirm_password = request.POST.get('confirm')
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)
        print(customer)
        flag = check_password(current_password, customer.password)
        if flag:
            if new_password == confirm_password:
                customer.password = make_password(new_password)
                customer.save()
                messages.success(request,"Password changed successfully")
                return redirect('Logout')
            else:
                error_message = "Both password doesn't match"
                return render(request, 'change_password.html', {'error': error_message})
        else:
            error_message = "YOU enterd the wrong password!!"
            return render(request, 'change_password.html', {'error': error_message})
