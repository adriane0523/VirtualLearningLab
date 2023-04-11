from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def shoppingPage_view(request, *args, **kwargs): 
  website_info = {
    "shoppingPage": "Welcome to the E-Learning-Lab Shoppify Page.",
    "description": "Here you can make transactions to buy any of our products!"
  }
  return render(request, "shoppifyPage_detail.html", website_info)
