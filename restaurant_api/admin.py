# --- File: restaurant_api/admin.py ---

from django.contrib import admin
from .models import MenuItem, Order, Feedback, OrderItem # Import all your models

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(OrderItem) # Register OrderItem as well for completeness
