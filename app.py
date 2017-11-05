#!/usr/bin/env python3

import sqlite3
import random
import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

RUNMODE = os.getenv('MEALMODE', default='dev')

app = Flask(__name__)
app.config.from_pyfile('config-' + RUNMODE + '.py')
db = SQLAlchemy(app)

class Meals(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(512), unique=True)
    protein = db.Column(db.String(256))
    season = db.Column(db.String(256))

admin = Admin(app, name='meals', template_mode='bootstrap3')
admin.add_view(ModelView(Meals, db.session))

@app.route('/')
def show():
    list_of_items = Meals.query.all()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    meals = []
    for item in range(5):
        meal_id = random.randint(0,len(list_of_items)-1)
        meals.append({'day': days[item], 'meal': list_of_items[meal_id].name})
        del list_of_items[meal_id]
    return render_template('index.html', meal_list=meals)

@app.route('/api')
def show_api():
    list_of_items = Meals.query.all()
    meal_id = random.randint(0,len(list_of_items)-1)
    found_item = {'meal': list_of_items[meal_id].name}
    return jsonify(found_item)


if __name__ == '__main__':
    app.run()
