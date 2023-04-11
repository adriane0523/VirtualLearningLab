from django.contrib import admin 
from django.urls import path 

from Components.shoppifyPage.views import shoppingPage_view

urlpatterns = [
  path('', shoppingPage_view, name="shoppifyPage")
]