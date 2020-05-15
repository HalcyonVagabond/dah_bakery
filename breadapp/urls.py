from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
    path('', bakery_home, name='bakery_home')
]
