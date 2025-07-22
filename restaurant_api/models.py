# --- File: restaurant_api/models.py ---

from django.db import models

class MenuItem(models.Model):
    """Represents a single item on the restaurant's menu."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50, default='Main') # e.g., 'Appetizer', 'Main', 'Dessert', 'Drink'
    is_available = models.BooleanField(default=True) # Can be toggled if item is out of stock
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    """Represents a customer's order."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup/Delivery'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    # Using a ManyToManyField with a 'through' model to store quantity for each item
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_time = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField(blank=True, null=True) # For scheduled pickups
    notes = models.TextField(blank=True, null=True) # Any special instructions

    def __str__(self):
        return f"Order {self.id} by {self.customer_name or 'Guest'} ({self.status})"

    def calculate_total(self):
        """Calculates the total amount of the order based on current OrderItems."""
        total = sum(item.menu_item.price * item.quantity for item in self.orderitem_set.all())
        self.total_amount = total
        self.save() # Save the updated total to the database

class OrderItem(models.Model):
    """Intermediate model for ManyToMany relationship between Order and MenuItem, storing quantity."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        # Ensures that a specific menu item can only be added once per order
        unique_together = ('order', 'menu_item')

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order {self.order.id}"

class Feedback(models.Model):
    """Represents customer feedback for an order or general experience."""
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True) # Optional link to an order
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)]) # 1 to 5 stars
    comment = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Order {self.order.id if self.order else 'N/A'} - Rating: {self.rating}"
