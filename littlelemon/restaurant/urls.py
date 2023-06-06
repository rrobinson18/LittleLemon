from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int>:pk', views.SingleMenuItemView.as_view()),
    # path('message/', views.msg)
]