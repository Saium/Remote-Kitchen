from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant, MenuCategory, MenuItem, Order
from .serializers import RestaurantSerializer, MenuCategorySerializer, MenuItemSerializer, OrderSerializer

class RestaurantListCreateView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)

class MenuCategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MenuCategory.objects.filter(restaurant__owner=self.request.user)

class MenuItemListCreateView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MenuItem.objects.filter(category__restaurant__owner=self.request.user)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
