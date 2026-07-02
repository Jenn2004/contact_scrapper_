import requests # pyright: ignore[reportMissingModuleSource]
from bs4 import BeautifulSoup # pyright: ignore[reportMissingImports]
import mysql.connector # pyright: ignore[reportMissingImports]

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",   # Replace with your actual password
    database="machine_test"
)

cursor = conn.cursor()

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

query = """
INSERT INTO news(title, link)
VALUES (%s, %s)
"""

for quote in quotes:
    title = quote.text
    link = url          # Store the page URL
    print(title)

    cursor.execute(query, (title, link))

conn.commit()

print("Data inserted successfully!")

cursor.execute("SELECT * FROM news")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()