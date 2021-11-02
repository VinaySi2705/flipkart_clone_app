from django.urls import path
from django.conf.urls import url,include
from clone.views import dashboard
from clone import views
urlpatterns = [
    # path('', views.Secr.home),
    path('',views.home),
    #path('categories', views.Secr.categories),
    path('categories',views.categories),
    # path('products/', views.Secr.products),
    path('products/',views.products),
    url(r"^accounts/",include("django.contrib.auth.urls")),
    # url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^dashboard/",dashboard,name="dashboard"),
]
