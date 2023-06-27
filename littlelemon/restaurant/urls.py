from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>', views.display_menu_items, name="menu_item"),
    path('bookings/', views.bookings, name="bookings"),
    # path('menu-items/', views.MenuItemView.as_view()),
    # path('menu-items/<int>:pk', views.SingleMenuItemView.as_view()),
    # path('message/', views.msg)
]