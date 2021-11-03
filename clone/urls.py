from django.urls import path
from . views import Index,Signup,Login,logout,Cart,Checkout,OrderView
from clone.middlewares.auth import auth_middleware
urlpatterns=[
    path('',Index.as_view(),name='homepage'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='Logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()),name='orders'),
]
