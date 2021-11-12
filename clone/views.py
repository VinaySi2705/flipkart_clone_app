from django.shortcuts import redirect, render
# Create your views here.
from django.contrib import messages

def logout(request):
    request.session.clear()
    messages.success(request,'Logged Out')
    return redirect('login')
