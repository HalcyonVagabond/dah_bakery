from .connection import Connection
from django.shortcuts import render, redirect, reverse
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
        ORDER BY b.name
        """)

        resp = db_cursor.fetchall()
        bread_inventory = []
        for i, item in enumerate(resp):
            bread = Bread()
            bread.id = item['id']
            bread.number = i + 1
            bread.name = item['name']
            bread.region = item['region']
            bread_inventory.append(bread)

        return bread_inventory

def post_bread(request):
    form_data = request.POST
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO breadapp_bread
        (name, region)
        VALUES (?, ?)
        """,
        (form_data['breadName'], form_data['breadRegion']))
    return redirect(reverse('breadapp:bakery_list'))

def bakery_list(request):
    if request.method == 'GET':
        bread_inventory = get_bread()
        template = 'bakery_list.html'
        context = {
            'bread_inventory': bread_inventory
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        return post_bread(request)