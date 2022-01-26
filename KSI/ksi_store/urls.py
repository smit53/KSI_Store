from django.contrib import admin
from django.urls import path
from ksi_store import views
from .views import *                  


app_name = 'ksi_store'


urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('Exclusives/',ItemListView.as_view(),name = 'Exclusive'),
    path('single_product/<int:id1>/', views.SingleProductView.as_view(), name="single_product"),
    # path('',views.IconView,name = 'icons'),
    path('cart/',views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    # path('update_item_clothings/',views.updateItemCLT, name = 'update_item_clothings'),
    path('contact/',views.contact,name='contact'),
    path('login',views.login_view,name = 'login_1'),
    path('email',views.send_mail, name='email'),
    path('register',views.register_user,name = 'register'),
    path('clothing',clothing.as_view(), name='cloth'),
    path('electronics',electronics.as_view(), name='electronics'),	
    path('grocery',grocery.as_view(), name='grocery'),	
    path('household',household.as_view(), name='household'),	
    path('sports',sports.as_view(), name='sports'),	
    path('vehical',vehical.as_view(), name='vehical'),
    path('mail',views.send_mail_django,name = 'mail'),
]