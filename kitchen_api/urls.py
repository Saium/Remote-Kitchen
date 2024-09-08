from django.urls import path
from .views import RestaurantListCreateView, MenuCategoryListCreateView, MenuItemListCreateView, OrderCreateView

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurants'),
    path('categories/', MenuCategoryListCreateView.as_view(), name='categories'),
    path('items/', MenuItemListCreateView.as_view(), name='items'),
    path('orders/', OrderCreateView.as_view(), name='orders'),
]
