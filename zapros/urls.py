from django.urls import path
from .views import *

urlpatterns = [
    path("", menu_view, name = "menu"),
]
