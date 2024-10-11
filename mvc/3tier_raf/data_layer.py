# data_layer.py

import sqlite3

def get_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_task_to_db(task_description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description) VALUES (?)', (task_description,))
    conn.commit()
    conn.close()


