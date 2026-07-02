import mysql.connector # pyright: ignore[reportMissingImports]

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="machine_test"
    )

    cursor = conn.cursor()

    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    age = int(input("Enter Age: "))
    sex = input("Enter Gender (M/F): ")
    income = int(input("Enter Income: "))

    query = """
    INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (fname, lname, age, sex, income)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Added Successfully!\n")

    cursor.execute("SELECT * FROM EMPLOYEE")

    print("Employee Records:")
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()