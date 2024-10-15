from flask import Blueprint, jsonify
import mysql.connector

main = Blueprint('main', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",   # We will change this to "db" in Docker setup
        user="your_user",
        password="your_password",
        database="fantasy_game_db"
    )

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Fantasy Game API!"})

@main.route('/characters')
def get_characters():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM characters")
    characters = cursor.fetchall()
    conn.close()
    return jsonify(characters)