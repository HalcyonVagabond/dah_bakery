from .connection import Connection
from django.shortcuts import render, redirect, reverse
import sqlite3
from ..models import Bread

def bakery_home(request):
    if request.method == 'GET':
        template = 'bakery_home.html'

        return render(request, template)
    
