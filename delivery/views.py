from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Restaurant
# Create your views here.
def index(request):
    return render(request, "delivery/index.html")
def open_signup(request):
    return render(request,"delivery/signup.html")

def open_signin(request):
    return render(request,"delivery/signin.html")


from django.shortcuts import render, redirect
from .models import Customer


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

            if customer.username.lower() == "admin":
                return render(request, "delivery/adminhome.html")

            return render(request, "delivery/success.html")

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
        rating = request.POST.get("rating", 0)

        image = request.FILES.get("image")

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

        return redirect("open_add_restaurant")

    return redirect("open_add_restaurant")


def open_show_restaurants(request):
    restaurants = Restaurant.objects.all()

    context = {
        "restaurants": restaurants
    }

    return render(request, "delivery/show_restaurants.html", context)