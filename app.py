import sqlite3
import os

API_KEY = "sk-prod-1234567890abcdef"  # secret hardcodé (à détecter)

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Injection SQL volontaire (à détecter)
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchone()

def run_command(cmd):
    # Command injection volontaire (à détecter)
    return os.system("echo " + cmd)

def healthcheck():
    return "OK"