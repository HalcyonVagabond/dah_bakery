from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
    path('', bakery_home, name='bakery_home'),
    path('list/', bakery_list, name='bakery_list'),
    path('bread/<int:bread_id>', bread_details, name='bread_details')

]
