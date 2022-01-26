import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','KSI.settings')
import django 
django. setup()
import random   
from ksi_store.models import Products

from faker import Faker
fakegen = Faker()
brand_electronics  =   ['Earphones','Smart Watches','Tablets','Phone','Laptop','Television']
brand_clothing     =   ['Tshirts','Shirts','Jeans','Tank tops','Sweatshirts','Shorts']
brand_grocery      =   ['Chips','Biscuits','Vegetables','Fruits','Breads','Cold Drinks']
brand_household    =   ['Mops','Vaccum Cleaner','Gloves','Chimney','Wardrobe','Sofas']
brand_sports       =   ['Sports_Shoes','Sports_Bags','Balls','Stability_Ball','Weights','Yoga Mat']
brand_vehicles     =   ['Bicycles','Booster Boards','Roller Skates','Segway','Cars','Bikes']
print("brnds inatialzied")

def pop(m=6):
    m=6
    print("for loop 1 called: ")
    for entry in range(m):
        S = brand_electronics[entry]

        name = S
        price = random.randrange(1000, 90000, 10000)
        # img =fakegen.image()
        S, Create = Products.objects.get_or_create(name=name, price=price)
        S.save()
        print("inside elect")
    print("data outside population exit Elect.......")

    print("for loop 2 called: ")

    for entry in range(m):
        S = brand_clothing[entry]

        name = S
        price = random.randrange(100, 9000, 500)
        # img =fakegen.image()
        S, Create = Products.objects.get_or_create(name=name, price=price)
        S.save()
        print("inside cloth")
    print("data ouside population Clothi.......")


    print("function called: ")
    for entry in range(m):
        S = brand_household[entry]

        name =S
        price = random.randrange(500, 15000,1000)
        # img =fakegen.image()
        S, Create = Products.objects.get_or_create(name=name, price=price)
        S.save()
        print("data inside Houehold.......")
    print("data outside population household.......")

    print("function called: ")
    for entry in range(m):
        S = brand_sports[entry]

        name = S
        price = random.randrange(2000, 10000,1000)
        # img =fakegen.image()
        S, Create = Products.objects.get_or_create(name=name, price=price)
        S.save()
        print("data inside population sports.......")
    print("data outside population happening.......")

    print("function called: ")
    for entry in range(m):
        S = brand_vehicles[entry]

        name = S
        price = random.randrange(100000, 4500000,700000)
        # img =fakegen.image()
        S, Create = Products.objects.get_or_create(name=name, price=price)
        S.save()
    print("data inside population vehicles.......")

    for entry in range(m):
        S = brand_grocery[entry]

        name = S
        price = random.randrange(1000, 90000, 10000)
        # img =fakegen.image()
        S, Create = Products.objects.get_or_create(name=name, price=price)
        S.save()
        print("inside elect")
    print("data outside population exit Elect.......")

    print("for loop 2 called: ")
print("data outside population happening.......")

#     print("function called: ")
#     for entry in range(m):      
#         S=brand[entry]
#         name=S
#         price=random.randrange(0,1000)      
#         S,Create = xyz.objects.get_or_create(name=name,price=price)
#         S.save()
#     print("data inside population happening.......")   
# print("data outside population happening.......")     

if __name__ == '__main__' :
    print("Populating the data please wait")
    pop()
    print("populating completed")