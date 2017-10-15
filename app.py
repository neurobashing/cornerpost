#!/usr/bin/env python3

import sqlite3
import random
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root@127.0.0.1/meals'
app.config['SECRET_KEY'] = 'dklfjsdlkfjslkdfjslkdfjslkdjfslkdjflskdjflksdjf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

if __name__ == '__main__':
    app.run()