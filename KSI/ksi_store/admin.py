from django.contrib import admin
from ksi_store.models import Products
from ksi_store.models import *



# Register your models here.
admin.site.register(Products)
admin.site.register (Customer)
admin.site.register (Order)
admin.site.register (OrderItem)
admin.site.register (ShippingAddress)
# admin.site.register(ContactUs)
admin.site.register(Electronics)
admin.site.register(Clothing)
admin.site.register(Grocery)
admin.site.register(Household)
admin.site.register(Sports)
admin.site.register(Vehicles)