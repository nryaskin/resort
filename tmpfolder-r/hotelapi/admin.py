from django.contrib import admin
from .models import Dishes, OrdersForToday, Procedures, Rooms, Visitors, Vocations

admin.site.register(Dishes)
admin.site.register(OrdersForToday)
admin.site.register(Procedures)
admin.site.register(Rooms)
admin.site.register(Visitors)
admin.site.register(Vocations)
