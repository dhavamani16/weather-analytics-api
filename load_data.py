import pandas as pd
import sqlite3
df=pd.read_csv('data/weather.csv')
df['date']=pd.to_datetime(df['date'])
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
df['day']=df['date'].dt.day
conn=sqlite3.connect("weather.db")
cursor=conn.cursor()
cursor.execute("""
    CREATE TABLE if NOT exists weather(
        date TEXT,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        temperature REAL,
        humidity REAL,
        pressure REAL,
        condition TEXT
        )""")
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['date'].strftime('%Y-%m-%d'),
        row['year'],
        row['month'],
        row['day'],
        row['temperature'],
        row['humidity'],
        row['pressure'],
        row.get('condition', 'Unknown')
    ))
conn.commit()
conn.close()
print("Data loaded Successfully")
