from django.db import models

#Create your models here.
class shoppingPage(models.Model): 

  #Shows the user information about product attributes
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True,null=True) # Product has description as text field
    price = models.TextField() # price has description as text field
    summary = models.TextField()

  #Function 1: (Need a way to redirect a user to the shopping page)
  

    #Note: Just remember to run command py manage.py makemigrations everytime you make changes to
    #migrations folder

  #Function 2: (Need a way for the user to place a order on the shopping page)


  #Function 3: (Need a way to place a confirmation message once user has placed order.)


