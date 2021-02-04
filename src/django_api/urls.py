from django.contrib import admin
from django.urls import path,include
from core.views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_frame