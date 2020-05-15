from .connection import Connection
from django.shortcuts import render, redirect, reverse
import sqlite3
from ..models import Bread, Ingredient


def get_bread(bread_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            b.id,
            b.name,
            b.region,
            bi.amount,
            i.name AS i_name,
            i.local_source
        FROM breadapp_bread AS b
        JOIN breadapp_breadingredient AS bi ON bi.bread_id = b.id
        JOIN breadapp_ingredient as i ON bi.ingredient_id = i.id
        WHERE b.id = ?
        """, (bread_id,))

        resp = db_cursor.fetchone()

        bread = Bread()
        bread.id = resp['id']
        bread.name = resp['name']
        bread.region = resp['region']
        
        print(resp)

        return bread

def bread_details(request, bread_id):
    if request.method == 'GET':
        bread = get_bread(bread_id)

        template = 'bread_details.html'
        context = {
            'bread': bread,
        }

        return render(request, template, context)