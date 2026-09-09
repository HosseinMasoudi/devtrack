import psycopg2

conn = psycopg2.connect(
    database="myproject",
    user="postgres",
    password="password",
    host="127.0.0.1",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT version()")

data = cursor.fetchone()

print("Connection established!")
print(data)

cursor.close()
conn.close()