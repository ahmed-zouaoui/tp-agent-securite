import sqlite3
import os

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Code volontairement sûr pour l'instant
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def healthcheck():
    return "OK"