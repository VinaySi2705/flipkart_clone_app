from django.urls import path
from . import views
urlpatterns = [
    path('', views.Secr.home),
    path('categories', views.Secr.categories),
    path('products/', views.Secr.all_products),


]
