# --- File: restaurant_api/urls.py ---

from rest_framework.routers import DefaultRouter
from django.urls import path # Import path
from .views import MenuItemViewSet, OrderViewSet, FeedbackViewSet, MenuView # Import MenuView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'feedback', FeedbackViewSet)

# The API URLs are now automatically determined by the router.
# Add custom URLs for templates or other views here
urlpatterns = router.urls + [ # Combine router URLs with custom paths
    path('menu_frontend/', MenuView.as_view(), name='menu_frontend'), # New URL for your menu.html
]
