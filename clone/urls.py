from django.urls import path
from . views import logout
from clone.view.index import Index
from clone.view.signup import Signup
from clone.view.checkout import Checkout
from clone.view.login import Login
from clone.view.cart import Cart
from clone.view.ordered import OrderView


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='Logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
]
