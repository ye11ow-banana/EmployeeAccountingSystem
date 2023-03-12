from django.contrib import admin
from django.urls import path, include

api_urls = [
    path('workers/', include('workers.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
