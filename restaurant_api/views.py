# --- File: restaurant_api/views.py ---

from rest_framework import viewsets
from django.views.generic import TemplateView # Import TemplateView
from .models import MenuItem, Order, Feedback
from .serializers import MenuItemSerializer, OrderSerializer, FeedbackSerializer

# API ViewSets (keep these as they are)
class MenuItemViewSet(viewsets.ModelViewSet):
    """API endpoint that allows menu items to be viewed or edited."""
    queryset = MenuItem.objects.all().order_by('category', 'name')
    serializer_class = MenuItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """API endpoint that allows orders to be viewed or edited."""
    queryset = Order.objects.all().order_by('-order_time')
    serializer_class = OrderSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    """API endpoint that allows feedback to be viewed or submitted."""
    queryset = Feedback.objects.all().order_by('-submitted_at')
    serializer_class = FeedbackSerializer

# New view for serving the menu.html template
class MenuView(TemplateView):
    """View to render the menu.html template."""
    template_name = 'menu.html' # Adjusted to your current path: restaurant_api/templates/menu.html
