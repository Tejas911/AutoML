from django.contrib import admin
from django.urls import path
from autopilot import views

urlpatterns = [
    path("", views.home),
]
