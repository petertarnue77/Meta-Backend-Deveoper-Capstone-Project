from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import permissions

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer


# Create your views here.
def home(request):
    return render(request, "index.html")


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
