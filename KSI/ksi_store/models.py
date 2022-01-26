from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Customer(models.Model):

#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='profile_user')

#     def __str__(self):
#         return self.user.username
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

class Customer (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    uname = models.CharField(max_length=200, null=True) 
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.uname



class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True, null=True) 
    transaction_id = models.CharField(max_length=200, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True) 
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.qunatity for item in orderitems])
        return total


class OrderItem(models.Model):

    product = models.ForeignKey(Products,on_delete=models.SET_NULL, blank=True, null=True)
    qunatity = models.IntegerField (default=0, null=True, blank=True) 
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models. SET_NULL, blank=True, null=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.qunatity
        return total



class ShippingAddress (models.Model):

    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True) 
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.address

# Models From simu
from django.db import models
from django.contrib.auth.models import User

class Electronics(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class Clothing(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

class Grocery(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

class Household(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
	
class Sports(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class Vehicles(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)

    img = models.ImageField(upload_to="ksi_store/",default = 'Ghantdi!!')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url