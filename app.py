#!/usr/bin/env python3

import sqlite3
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def show():
	conn = sqlite3.connect('food.db')

	c = conn.cursor()  # our cursor

	results = c.execute('select name from meals').fetchall()
	list_of_items = [name[0] for name in results]

	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

	meals = []
	for item in range(5):
		meal_id = random.randint(0,len(list_of_items)-1)
		meals.append({'day': days[item], 'meal': list_of_items[meal_id]})
		del list_of_items[meal_id]
	conn.close()
	return render_template('index.html', meal_list=meals)

if __name__ == '__main__':
    app.run()