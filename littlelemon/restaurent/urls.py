from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.MenuItemView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-item"),
    path("api-token-auth/", obtain_auth_token),
]
