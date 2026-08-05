from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("open_signup", views.open_signup, name="open_signup"),
    path("open_signin", views.open_signin, name="open_signin"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("open_add_restaurant",views.open_add_restaurant,name="open_add_restaurant",),
    path("add_restaurant",views.add_restaurant,name="add_restaurant",),
    path("open_show_restaurants", views.open_show_restaurants, name="open_show_restaurants"),
    path("open_update_restaurant/<int:id>",views.open_update_restaurant,name="open_update_restaurant",),
    path('update_restaurant/<int:id>/', views.update_restaurant, name='update_restaurant'),
    path('delete-restaurant/<int:id>/', views.delete_restaurant, name='delete_restaurant'),
    path("restaurants/", views.open_show_restaurants, name="restaurants"),
    path("open_add_menu/<int:restaurant_id>/",views.open_add_menu,name="open_add_menu",),
    path("add_menu/<int:restaurant_id>/", views.add_menu, name="add_menu"),
    path(
    "open_update_menu/<int:id>/",
    views.open_update_menu,
    name="open_update_menu",
),

path(
    "update_menu/<int:id>/",
    views.update_menu,
    name="update_menu",
),
path(
    "customer_home/",
    views.customer_home,
    name="customer_home"
),
path(
    "show_menu/<int:restaurant_id>/",
    views.show_menu,
    name="show_menu",
),
path(
    "show_menu/<int:restaurant_id>/",
    views.show_menu,
    name="show_menu",
),
path("cart/", views.cart, name="cart"),

path(
    "add_to_cart/<int:menu_id>/",
    views.add_to_cart,
    name="add_to_cart",
),

path(
    "cart/",
    views.cart,
    name="cart",
),
path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
path("checkout/", views.checkout, name="checkout"),
path(
    "checkout/",
    views.checkout,
    name="checkout",
),
path("checkout/", views.checkout, name="checkout"),
    ]