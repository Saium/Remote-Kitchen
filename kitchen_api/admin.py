from django.contrib import admin

# Register your models here

from .models import Restaurant,  Order, MenuCategory, MenuItem, Order

admin.site.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ['name', 'owner']


admin.site.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    model = MenuCategory
    list_display = ['name', 'restaurant']



admin.site.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ['name', 'price', 'category']

    