import sqlite3
from datetime import datetime, timedelta

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
sql = "INSERT INTO flights (origin_city, destination_city, airline, depart_date, available_seates, price) VALUES (?, ?, ?, ?, ?, ?)"
data = [
    ('London', 'Tokyo', 'British Airways', datetime.now() + timedelta(1), 100, 120),
    ('New York', 'Tokyo', 'British Airways', datetime.now() + timedelta(1), 100, 130),
    ('Paris', 'Tokyo', 'British Airways', datetime.now() + timedelta(1), 100, 100),
    ('London', 'Rome', 'British Airways', datetime.now() + timedelta(1), 100, 60),
    ('New York', 'Rome', 'British Airways', datetime.now() + timedelta(1), 100, 300),
    ('Paris', 'Rome', 'British Airways', datetime.now() + timedelta(1), 100, 40),
    ('London', 'Berlin', 'British Airways', datetime.now() + timedelta(1), 100, 50),
    ('New York', 'Berlin', 'British Airways', datetime.now() + timedelta(1), 100, 300),
    ('Paris', 'Berlin', 'British Airways', datetime.now() + timedelta(1), 100, 30),
    ('London', 'Tokyo', 'Emirates', datetime.now() + timedelta(1), 100, 200),
    ('New York', 'Tokyo', 'Emirates', datetime.now() + timedelta(1), 100, 500),
    ('Paris', 'Tokyo', 'Emirates', datetime.now() + timedelta(1), 100, 300),
    ('London', 'Rome', 'Emirates', datetime.now() + timedelta(1), 100, 70),
    ('New York', 'Rome', 'Emirates', datetime.now() + timedelta(1), 100, 400),
    ('Paris', 'Rome', 'Emirates', datetime.now() + timedelta(1), 100, 40),
    ('London', 'Berlin', 'Emirates', datetime.now() + timedelta(1), 100, 50),
    ('New York', 'Berlin', 'Emirates', datetime.now() + timedelta(1), 100, 80),
    ('Paris', 'Berlin', 'Emirates', datetime.now() + timedelta(1), 100, 100),
    ('London', 'Tokyo', 'KLM', datetime.now() + timedelta(1), 100, 60),
    ('New York', 'Tokyo', 'KLM', datetime.now() + timedelta(1), 100, 800),
    ('Paris', 'Tokyo', 'KLM', datetime.now() + timedelta(1), 100, 30),
    ('London', 'Rome', 'KLM', datetime.now() + timedelta(1), 100, 40),
    ('New York', 'Rome', 'KLM', datetime.now() + timedelta(1), 100, 60),
    ('Paris', 'Rome', 'KLM', datetime.now() + timedelta(1), 100, 50),
    ('London', 'Berlin', 'KLM', datetime.now() + timedelta(1), 100, 90),
    ('New York', 'Berlin', 'KLM', datetime.now() + timedelta(1), 100, 100),
    ('Paris', 'Berlin', 'KLM', datetime.now() + timedelta(1), 100, 500),
]
for i in data:
    cur.execute(sql,i)

print("Database initialized")

connection.commit()
connection.close()
