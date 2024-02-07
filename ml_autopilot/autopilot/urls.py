from django.contrib import admin
from django.urls import path
from autopilot import views

urlpatterns = [
    path("", views.home, name="home"),
    path("process-options/", views.process_options, name="process_options"),
    # path("auto/<str:target>/", views.auto_page, name="auto_page"),
    # path("manual/<str:target>/", views.manual_page, name="manual_page"),
]
