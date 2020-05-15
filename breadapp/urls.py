from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
    path('', bakery_home, name='bakery_home'),
    path('home/', bakery_home, name='bakery_home'),
    path('bread/<int:bread_id>', bread_details, name='bread_details')

]
