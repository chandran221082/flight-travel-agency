import sqlite3
from datetime import datetime

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
sql = "INSERT INTO flights (origin_city, destination_city, airline, depart_date, available_seates) VALUES (?, ?, ?, ?, ?)"
data = [
    ('London', 'Tokyo', 'British Airways', datetime(2024, 2, 23, 14, 30), 100),
    ('New York', 'Tokyo', 'British Airways', datetime(2024, 2, 23, 15, 30), 100),
    ('Paris', 'Tokyo', 'British Airways', datetime(2024, 2, 23, 16, 30), 100),
    ('London', 'Rome', 'British Airways', datetime(2024, 2, 23, 17, 30), 100),
    ('New York', 'Rome', 'British Airways', datetime(2024, 2, 23, 18, 30), 100),
    ('Paris', 'Rome', 'British Airways', datetime(2024, 2, 23, 14, 00), 100),
    ('London', 'Berlin', 'British Airways', datetime(2024, 2, 23, 15, 00), 100),
    ('New York', 'Berlin', 'British Airways', datetime(2024, 2, 23, 16, 40), 100),
    ('Paris', 'Berlin', 'British Airways', datetime(2024, 2, 23, 17, 40), 100),
    ('London', 'Tokyo', 'Emirates', datetime(2024, 2, 23, 18, 20), 100),
    ('New York', 'Tokyo', 'Emirates', datetime(2024, 2, 23, 11, 30), 100),
    ('Paris', 'Tokyo', 'Emirates', datetime(2024, 2, 24, 14, 30), 100),
    ('London', 'Rome', 'Emirates', datetime(2024, 2, 23, 14, 30), 100),
    ('New York', 'Rome', 'Emirates', datetime(2024, 2, 23, 14, 30), 100),
    ('Paris', 'Rome', 'Emirates', datetime(2024, 2, 23, 14, 30), 100),
    ('London', 'Berlin', 'Emirates', datetime(2024, 2, 23, 14, 30), 100),
    ('New York', 'Berlin', 'Emirates', datetime(2024, 2, 23, 14, 30), 100),
    ('Paris', 'Berlin', 'Emirates', datetime(2024, 2, 23, 14, 30), 100),
    ('London', 'Tokyo', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('New York', 'Tokyo', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('Paris', 'Tokyo', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('London', 'Rome', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('New York', 'Rome', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('Paris', 'Rome', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('London', 'Berlin', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('New York', 'Berlin', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
    ('Paris', 'Berlin', 'KLM', datetime(2024, 2, 23, 14, 30), 100),
]
for i in data:
    cur.execute(sql,i)

connection.commit()
connection.close()
