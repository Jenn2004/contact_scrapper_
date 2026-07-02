import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="machine_test"
)

cursor = conn.cursor()

# Read data from news table
cursor.execute("""
SELECT portalid, town, news, date
FROM news
""")

rows = cursor.fetchall()

print("News Table Data\n")

for row in rows:
    print(row)

print("\nCopying records...\n")

insert_query = """
INSERT INTO kf_docmnt(portalid, town, news, date)
VALUES(%s,%s,%s,%s)
"""

for row in rows:
    cursor.execute(insert_query, row)

conn.commit()

print("Records copied successfully!")

print("\nData in kf_docmnt\n")

cursor.execute("SELECT * FROM kf_docmnt")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()