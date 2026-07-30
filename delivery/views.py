from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
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