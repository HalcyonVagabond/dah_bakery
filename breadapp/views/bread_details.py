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
        LEFT JOIN breadapp_breadingredient AS bi ON bi.bread_id = b.id
        LEFT JOIN breadapp_ingredient as i ON bi.ingredient_id = i.id
        WHERE b.id = ?
        """, (bread_id,))

        response = db_cursor.fetchall()

        for row in response:
            print("ROW!!!!!!")
            print(row)            
        bread = Bread()
        bread.ingredient_list = []
        for row in response:
            if row == response[0]:
                bread.id = row['id']
                bread.name = row['name']
                bread.region = row['region']
                if not row['i_name'] == None:
                    ingredient = Ingredient()
                    ingredient.name = row['i_name']
                    ingredient.local_source = row['local_source']
                    bread.ingredient_list.append(ingredient)
            else:
                ingredient = Ingredient()
                ingredient.name = row['i_name']
                ingredient.amount = row['amount']
                ingredient.local_source = row['local_source']
                bread.ingredient_list.append(ingredient)
        
        bread.length = len(bread.ingredient_list)
        return bread
        
        

def bread_details(request, bread_id):
    if request.method == 'GET':
        bread = get_bread(bread_id)

        template = 'bread_details.html'
        context = {
            'bread': bread,
        }

        return render(request, template, context)