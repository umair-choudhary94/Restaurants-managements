from django.contrib import admin
from .models import restaurant, fooditem,MyUser,table,bookingrecord,foodorder,restaurantcategories

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'min_price', 'max_price', 'tables', 'seats']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'title', 'price']
class detailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone']
class tablesAdmin(admin.ModelAdmin):
    list_display = ['id','restaurant', 'seats', 'booking_status']
class bookAdmin(admin.ModelAdmin):
    list_display = ['id','user','restaurant', 'table', 'timestamp']

class ordersAdmin(admin.ModelAdmin):
    list_display = ['id','item','user', 'bill', 'timestamp',"order_status"]

admin.site.register(restaurant, RestaurantAdmin)
admin.site.register(MyUser, detailsAdmin)
admin.site.register(table, tablesAdmin)
admin.site.register(bookingrecord, bookAdmin)
admin.site.register(foodorder, ordersAdmin)
admin.site.register(fooditem, FoodAdmin)
admin.site.register(restaurantcategories)

