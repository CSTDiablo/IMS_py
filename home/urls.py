from django.urls import path
from .views import (home, staff,products,)

urlpatterns = [
    path('',home , name='IMS-Home'),
    path('staff/', staff , name='IMS-Staff'),
    path('products/', products, name='IMS-Products')
]
