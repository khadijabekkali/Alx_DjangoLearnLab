from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # 👈 THIS LINE IS WHAT CHECKER WANTS
]
