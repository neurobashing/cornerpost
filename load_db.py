#!/usr/bin/env python3

from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column
from sqlalchemy_utils import database_exists, create_database, drop_database
import os
import sys

RUNMODE = os.getenv('MEALMODE', default='dev')

if RUNMODE == "dev":
    db_uri = 'mysql+mysqldb://root@127.0.0.1/meals'
elif RUNMODE == 'production':
    db_uri = 'mysql+mysqldb://root:goldcoin@127.0.0.1/meals'
else:
    print("You have made a massive mistake. You do not have a valid RUNMODE env var.")
    sys.exit()

if database_exists(db_uri):
    drop_database(db_uri)
    create_database(db_uri)
else:
    create_database(db_uri)

engine = create_engine(db_uri)
conn = engine.connect()

metadata = MetaData()

metadata.drop_all(engine)

# TODO ugh must keep in sync with app, but flask-sqlalchemy != sqlalchemy
meals = Table('meals', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(512), unique=True),
    Column('protein', String(256)),
    Column('season', String(256)))

metadata.create_all(engine)

with open('source.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
for item in content:
    print("Inserting " + item)
    meal = meals.insert().values(name=item)
    conn.execute(meal)
