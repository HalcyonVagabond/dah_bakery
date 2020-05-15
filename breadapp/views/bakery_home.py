from .connection import Connection
from django.shortcuts import render
import sqlite3
from ..models import Bread


def get_bread():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            b.id,
            b.name,
            b.region
        FROM breadapp_bread AS b
        """)

        resp = db_cursor.fetchall()
        bread_inventory = []
        for item in resp:
            bread = Bread()
            bread.id = item['id']
            bread.name = item['name']
            bread.region = item['region']
            bread_inventory.append(bread)

        return bread_inventory

def bakery_home(request):
    if request.method == 'GET':
        bread_inventory = get_bread()
        template = 'bakery_home.html'
        context = {
            'bread_inventory': bread_inventory
        }

        return render(request, template, context)