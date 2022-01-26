from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .form import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.urls import reverse
from django.views.generic import ListView,View,TemplateView
from .models import Products,Order,OrderItem,Customer,Clothing,Electronics,Grocery,Household,Sports,Vehicles
from . import models
from django.http import JsonResponse
import json
# Contact
from .form import ContactForm
from django.core.mail import send_mail

# from django.core.mail import send_mail


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class ItemListView(ListView):
    context_object_name = 'product'
    model = models.Products
    template_name = 'Exclusive.html'

def send_mail_django(request):
    # send_mail_task()
    # return HttpResponseRedirect(reverse('index'))

    print('in the mail func')
    email= request.user.email
    print('email',email)
    a = OrderItem.objects.all()
    print('a: ',a)
    subject= "Recent Purchased"
    print('subject',subject)

    message ="You\'re order is saved into our darabase.Thank you for purchasing from us..😊😊"
    print('message',message)
    send_mail(subject, message,'KSI.3buckcoders@gmail.com' , [email])
    print('Mail has been sent!!')

    a.delete()
    print('a: ',a)

    return HttpResponseRedirect(reverse('index'))


    

#CART
def updateItem(request):

    data = json.loads (request.body) 
    productId= data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:',productId) 

    customer = request.user.customer
    print('customer',customer)

    product = Products.objects.get(id=productId)
    print('product',product)

    order, created = Order.objects.get_or_create(customer=customer)
    print('order',order)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    print('order_item',order_item)
    
    if action=="add":
        order_item.qunatity = (order_item.qunatity +1)
    elif action == "remove":
        order_item.qunatity = (order_item.qunatity-1)
    order_item.save()

    if order_item.qunatity <=0:
        order_item.delete()
    return JsonResponse("Item was added", safe=False)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print('order',order)

        items = order.orderitem_set.all()
        print('items',items)

        cartItems = order.get_cart_items
        print('cartItems',cartItems)

    else:
        items = []
    context = {'items': items,'order':order, 'cartItems':cartItems}
    return render(request,'cart.html',context)
    
class SingleProductView(View):

    def get(self, request, id1, *args, **kwargs):
    
        object_1 = get_object_or_404(models.Products, pk = id1)
        pk = id1
        # products = models.Products.objects.filter(is_deleted=False).exclude(pk=id1).filter()
        return render(request, 'single_product.html', context={
            'object_1': object_1,
            'pk':pk
        })

@login_required(login_url='login.html')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = '<h4>Wait till the authorizations from the admin!</h4>'
            success = True
            send_mail('New user registration', username+'Plz Accept me' , 'KSI.3buckcoders@gmail.com', ['KSI.3buckcoders@gmail.com'])

            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })

#Contact info


def contact(request):
    name=''
    email=''
    subject=''
    message=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        subject=form.cleaned_data.get("subject")
        message= form.cleaned_data.get("message")


        # if request.user.is_authenticated():
        #     subject= str(request.user) + "'s message"
        # else:
        #     subject= "A Visitor's message"


        content= name + " with the email, " + email + ", sent the following message:\n\n" + message;
        send_mail(subject, content, email,['KSI.3buckcoders@gmail.com'] )

        # context= {'form': form}

        context= {'name':name,'email':email,'subject':subject,'message':message}

        return render(request, 'contact.html', context)

    else:
        context= {'name':name,'email':email,'subject':subject,'message':message}
        # context= {'form': form}
        return render(request, 'contact.html', context)

#  Sub Pages 
class clothing(ListView):
    context_object_name = 'cloth'
    model = models.Products
    template_name = 'clothing.html'

# def clothing(request):

#     clthing = Clothing.objects.all()
#     context = {'clthing':clthing}
#     return render(request,'clothing.html',context)

# Individual cart
class electronics(ListView):
    context_object_name = 'electronics'
    model = models.Products
    template_name = 'electronics.html'

class grocery(ListView):
    context_object_name = 'grocery'
    model = models.Products
    template_name = 'grocery.html'

class household(ListView):
    context_object_name = 'household'
    model = models.Products
    template_name = 'household.html'

class sports(ListView):
    context_object_name = 'sports'
    model = models.Products
    template_name = 'sports.html'

class vehical(ListView):
    context_object_name = 'vehical'
    model = models.Products
    template_name = 'vehical.html'

# def electronics(request):
#     return render(request,'electronics.html',{})

# def grocery(request):
#     return render(request,'grocery.html',{})

# def household(request):
#     return render(request,'household.html',{})

# def sports(request):
#     return render(request,'sports.html',{})

# def vehical(request):
#     return render(request,'vehical.html',{})
    
# def contact(request):


#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         return render(request, 'contact.html', {'name': name})
#     else:
#         return render(request, 'contact.html', {})
