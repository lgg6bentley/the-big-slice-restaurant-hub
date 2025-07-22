# --- File: the_big_slice_restaurant_hub/urls.py ---
# (Modify your existing urls.py file)

from django.contrib import admin
from django.urls import path, include # Ensure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restaurant_api.urls')), # Include your API app's URLs
]
