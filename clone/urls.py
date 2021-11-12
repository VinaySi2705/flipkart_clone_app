from django.urls import path
from . views import logout 
from clone.view.index import Index
from clone.view.signup import Signup
from clone.view.checkout import Checkout
from clone.view.login import Login
from clone.view.cartview import Cart
from clone.view.ordered import OrderView
from clone.view.change_password import ChangePassword
from clone.middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='Logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', auth_middleware(Checkout.as_view()), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('change_password', auth_middleware(ChangePassword.as_view())),
]
