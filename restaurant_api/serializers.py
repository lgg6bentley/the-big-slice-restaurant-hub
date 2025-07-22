# --- File: restaurant_api/serializers.py ---

from rest_framework import serializers
from .models import MenuItem, Order, OrderItem, Feedback

class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer for the MenuItem model."""
    class Meta:
        model = MenuItem
        fields = '__all__' # Include all fields from the model

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the OrderItem model, used for nested representation within Order."""
    menu_item_name = serializers.ReadOnlyField(source='menu_item.name')
    price_at_order = serializers.ReadOnlyField(source='menu_item.price') # Capture price at time of order

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity', 'price_at_order']
        read_only_fields = ['menu_item_name', 'price_at_order'] # These fields are derived, not set by user

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model, including nested OrderItems."""
    # 'source' points to the reverse relationship name from OrderItem to Order
    # 'many=True' indicates it's a list of OrderItem objects
    # 'read_only=True' means these items are displayed but not created/updated directly via this serializer
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__' # Includes all fields like customer_name, total_amount, status, etc.

class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer for the Feedback model."""
    class Meta:
        model = Feedback
        fields = '__all__'
