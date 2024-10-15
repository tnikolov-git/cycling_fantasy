import os

class Config:
    MYSQL_HOST = os.getenv('DB_HOST', 'localhost')
    MYSQL_USER = os.getenv('DB_USER', 'your_user')
    MYSQL_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')
    MYSQL_DB = os.getenv('DB_NAME', 'fantasy_game_db')