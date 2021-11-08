from django.shortcuts import redirect
# Create your views here.


def logout(request):
    request.session.clear()
    return redirect('login')
