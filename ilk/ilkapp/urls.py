from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    
    path('', include('ilkapp.urls')),
    path('admin/', admin.site.urls),
    path('', include('ilk.urls')),
]