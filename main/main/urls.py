from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('demo.urls')),
    path('DemoDjango', include('demo.urls')),
]
