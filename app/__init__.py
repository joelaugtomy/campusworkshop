"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpreb0rddl9mmoj5kcg-a.oregon-postgres.render.com",
        database="todo_pd1t",
        user="root",
        password="TP1xOFTsa3zPz8hQ2X7YQC0pxXVBzlhj")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
