from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Restaurant,Menu,Cart
# Create your views here.
def index(request):
    return render(request, "delivery/index.html")
def open_signup(request):
    return render(request,"delivery/signup.html")

def open_signin(request):
    return render(request,"delivery/signin.html")


from django.shortcuts import render, redirect,get_object_or_404
from .models import Customer, Restaurant


# def signup(request):
#     if request.method == "POST":


#         email = request.POST.get("email")
#         username = request.POST.get("username")
#         mobile = request.POST.get("mobile")
#         address = request.POST.get("address")

#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")

#         if password1 != password2:
#             return render(request, "delivery/signup.html", {
#                 "error": "Passwords do not match"
#             })

#         try:
#             Customer.objects.get(username=username)
#             return render(request, "delivery/signup.html", {
#                 "error": "Username already exists"
#             })

#         except Customer.DoesNotExist:

#             Customer.objects.create(
                
#                 email=email,
#                 username=username,
#                 mobile=mobile,
#                 address=address,
#                 password=password1
#             )

#             return redirect("/")


#     return render(request, "delivery/signin.html")




def signup(request):
    if request.method == "POST":

        email = request.POST.get("email")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check password match
        if password1 != password2:
            return render(request, "delivery/signup.html", {
                "error": "Passwords do not match."
            })

        # Check if username already exists
        if Customer.objects.filter(username=username).exists():
            return render(request, "delivery/signup.html", {
                "error": "Username already exists."
            })

        # Create new customer
        Customer.objects.create(
            email=email,
            username=username,
            mobile=mobile,
            address=address,
            password=password1
        )

        return redirect("open_signin")

    return render(request, "delivery/signup.html")

# def signin(request):
#     if request.method == 'POST':

#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             Customer.objects.get(username=username, password=password)

#             if username.lower() == 'admin':
#                 return render(request, 'delivery/adminhome.html')
#             else:
#                 return render(request, 'delivery/success.html')

#         except Customer.DoesNotExist:
#             return render(request, 'delivery/fail.html')

#     return render(request, 'delivery/signin.html')

# Sign In
def signin(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            customer = Customer.objects.get(
                username=username,
                password=password
            )

            # Save customer id in session
            request.session["customer_id"] = customer.id

            if customer.username.lower() == "admin":
                return render(request, "delivery/adminhome.html")

            return redirect("customer_home")

        except Customer.DoesNotExist:
            return render(request, "delivery/signin.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "delivery/signin.html")



def open_add_restaurant(request):
    return render(request, "delivery/add_restaurants.html")



def add_restaurant(request):
    if request.method == "POST":

        restaurant_name = request.POST.get("restaurant_name")
        owner_name = request.POST.get("owner_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        cuisine = request.POST.get("cuisine")
        opening_time = request.POST.get("opening_time")
        closing_time = request.POST.get("closing_time")

        # Get image URL from the form
        image = request.POST.get("image")

        # Use a default image if no URL is provided
        if not image:
            image = "https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg"

        Restaurant.objects.create(
            restaurant_name=restaurant_name,
            owner_name=owner_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            pincode=pincode,
            cuisine=cuisine,
            opening_time=opening_time,
            closing_time=closing_time,
            image=image
        )

        return redirect("open_show_restaurants")

    return redirect("open_add_restaurant")


def open_show_restaurants(request):
    restaurants = Restaurant.objects.all()

    context = {
        "restaurants": restaurants
    }

    return render(request, "delivery/show_restaurants.html", context)


def open_update_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)

    return render(
        request,
        "delivery/update_restaurant.html",
        {"restaurant": restaurant}
    )


def update_restaurant(request, id):

    restaurant = Restaurant.objects.get(id=id)

    if request.method == "POST":

        restaurant.restaurant_name = request.POST.get("restaurant_name")
        restaurant.owner_name = request.POST.get("owner_name")
        restaurant.email = request.POST.get("email")
        restaurant.phone = request.POST.get("phone")
        restaurant.address = request.POST.get("address")
        restaurant.city = request.POST.get("city")
        restaurant.pincode = request.POST.get("pincode")
        restaurant.cuisine = request.POST.get("cuisine")
        restaurant.opening_time = request.POST.get("opening_time")
        restaurant.closing_time = request.POST.get("closing_time")
        restaurant.image = request.POST.get("image")

        restaurant.save()

        return redirect("open_show_restaurants")

    return render(
        request,
        "delivery/update_restaurant.html",
        {"restaurant": restaurant}
    )


def delete_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)

    if request.method == "POST":
        restaurant.delete()
        return redirect("open_show_restaurants")

    return render(
        request,
        "delivery/delete_restaurant.html",
        {"restaurant": restaurant}
    )

def open_add_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(
        request,
        "delivery/add_menu.html",
        {"restaurant": restaurant},
    )

def add_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        Menu.objects.create(
            restaurant=restaurant,
            item_name=request.POST.get("item_name"),
            price=request.POST.get("price"),
            category=request.POST.get("category"),
            description=request.POST.get("description"),
            image=request.POST.get("image"),
        )

        return redirect("open_show_restaurants")

    return redirect("open_add_menu", restaurant_id=restaurant.id)

from django.shortcuts import get_object_or_404, render, redirect

def open_update_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    return render(
        request,
        "delivery/update_menu.html",
        {"menu": menu}
    )


def update_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == "POST":
        menu.item_name = request.POST.get("item_name")
        menu.price = request.POST.get("price")
        menu.category = request.POST.get("category")
        menu.description = request.POST.get("description")
        menu.image = request.POST.get("image")

        menu.save()

        return redirect("open_show_restaurants")

    return render(
        request,
        "delivery/update_menu.html",
        {"menu": menu}
    )

from datetime import datetime
from django.db.models import Q

from datetime import datetime
from django.db.models import Q

def customer_home(request):

    customer_id = request.session.get("customer_id")

    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        customer_name = customer.username
    else:
        customer_name = "Customer"

    # Greeting
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    elif hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    restaurants = Restaurant.objects.all()

    # Search
    search = request.GET.get("search")

    if search:
        restaurants = restaurants.filter(
            Q(restaurant_name__icontains=search) |
            Q(cuisine__icontains=search) |
            Q(menus__item_name__icontains=search) |
            Q(menus__category__icontains=search)
        ).distinct()

    # Category
    category = request.GET.get("category")

    if category:
        restaurants = restaurants.filter(
            Q(cuisine__icontains=category) |
            Q(menus__category__icontains=category) |
            Q(menus__item_name__icontains=category)
        ).distinct()

    return render(
        request,
        "delivery/customer_home.html",
        {
            "restaurants": restaurants,
            "greeting": greeting,
            "customer_name": customer_name,
        }
    )

from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Menu

def show_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menus = Menu.objects.filter(restaurant=restaurant)

    return render(
        request,
        "delivery/show_menu.html",
        {
            "restaurant": restaurant,
            "menus": menus,
        },
    )

def show_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menus = Menu.objects.filter(restaurant=restaurant)

    return render(
        request,
        "delivery/show_menu.html",
        {
            "restaurant": restaurant,
            "menus": menus,
        }
    )

def cart(request):
    return render(
        request,
        "delivery/cart.html",
        {
            "cart_items": [],
            "grand_total": 0
        }
    )

def add_to_cart(request, menu_id):

    menu = get_object_or_404(Menu, id=menu_id)

    customer = Customer.objects.get(
    id=request.session["customer_id"]
)

    cart_item = Cart.objects.filter(
        customer=customer,
        menu=menu
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(
            customer=customer,
            menu=menu,
            quantity=1
        )

    return redirect("cart")

def cart(request):

    customer = Customer.objects.get(
    id=request.session["customer_id"]
)

    cart_items = Cart.objects.filter(customer=customer)

    grand_total = 0

    for item in cart_items:
        grand_total += item.quantity * item.menu.price

    return render(
        request,
        "delivery/cart.html",
        {
            "cart_items": cart_items,
            "grand_total": grand_total
        }
    )

from django.shortcuts import get_object_or_404, redirect

def remove_from_cart(request, item_id):

    customer_id = request.session.get("customer_id")

    if customer_id is None:
        return redirect("open_signin")

    customer = get_object_or_404(Customer, id=customer_id)

    item = get_object_or_404(
        Cart,
        id=item_id,
        customer=customer
    )

    item.delete()

    return redirect("cart")

from .models import Order, OrderItem

def checkout(request):
    customer = get_object_or_404(
        Customer,
        id=request.session["customer_id"]
    )

    cart_items = Cart.objects.filter(customer=customer)

    if not cart_items.exists():
        return redirect("cart")

    grand_total = sum(item.quantity * item.menu.price for item in cart_items)

    order = Order.objects.create(
        customer=customer,
        total_amount=grand_total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            menu=item.menu,
            quantity=item.quantity,
            price=item.menu.price
        )

    # Empty the cart
    cart_items.delete()

    return render(request, "delivery/order_success.html", {
        "order": order
    })

import razorpay
from django.conf import settings

def checkout(request):

    customer = Customer.objects.get(
        id=request.session["customer_id"]
    )

    cart_items = Cart.objects.filter(customer=customer)

    grand_total = sum(
        item.quantity * item.menu.price
        for item in cart_items
    )

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({
        "amount": int(grand_total * 100),
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        "cart_items": cart_items,
        "total_price": grand_total,
        "amount": payment["amount"],
        "order_id": payment["id"],
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "username": customer.username,
    }

    return render(
        request,
        "delivery/checkout.html",
        context
    )