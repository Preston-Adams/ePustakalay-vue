"""
URLPATTERNS for management apps.
"""
from django.urls import path
from management import views

urlpatterns = [
    path('', views.index),
]
