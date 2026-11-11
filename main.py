import mysql.connector as sql

# ==========================================
# Part 1: File Handling (Text File)
# ==========================================

# Create and write to pantry.txt
try:
    file = open("pantry.txt", "w")
    file.write("ItemName,Category,Quantity\n")
    file.write("Rice,Grains,2\n")
    file.write("Milk,Dairy,1\n")
    file.write("Eggs,Dairy,12\n")
    file.write("Sugar,Grains,2\n")
    file.write("Salt,Grains,1\n")
    file.write("Toast,Bakery,1\n")
    file.write("Cheese,Dairy,3\n")
    file.write("Apples,Fruits,7\n")
    file.write("Tomatoes,Vegetables,10\n")
    file.write("Oranges,Fruits,5\n")
    file.close()
    print("pantry.txt file created successfully")
except Exception as e:
    print("Error", e)

# Read from pantry.txt
try:
    file = open("pantry.txt", "r")
    print("\nThe pantry.txt File")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print("Error", e)


# ==========================================
# Part 2: Convert Data into MySQL Database
# ==========================================

# 1. Create Database
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE"
    )
    cur = myconn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS pantry_db")
    print("Database created successfully.")
    myconn.close()
except Exception as e:
    print("error:", e)

# 2. Create Table
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",
        database="pantry_db"
    )
    cur = myconn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS pantry_items(
        id INT AUTO_INCREMENT PRIMARY KEY,
        item_name VARCHAR(100),
        category VARCHAR(100),
        quantity INT
    )""")
    print("Table created successfully.")
    myconn.close()
except Exception as e:
    print("Error:", e)

# 3. Show Databases
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE"
    )
    cur = myconn.cursor()
    cur.execute("SHOW DATABASES")
    print("\nDatabases:")
    for db in cur:
        print(db)
    myconn.close()
except Exception as e:
    print("Error:", e)

# 4. Show Tables
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",
        database="pantry_db"
    )
    cur = myconn.cursor()
    cur.execute("SHOW TABLES")
    print("\nTables in pantry_db:")
    for table in cur:
        print(table)
    myconn.close()
except Exception as e:
    print("Error:", e)

# 5. Insert Data (executemany)
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",
        database="pantry_db"
    )
    cur = myconn.cursor()
    
    insert_sql = "INSERT INTO pantry_items(item_name, category, quantity) VALUES (%s, %s, %s)"
    values = [
        ("Rice", "Grains", 2),
        ("Milk", "Dairy", 1),
        ("Eggs", "Dairy", 12),
        ("Sugar", "Grains", 2),
        ("Salt", "Grains", 1),
        ("Toast", "Bakery", 1),
        ("Cheese", "Dairy", 3),
        ("Apples", "Fruits", 7),
        ("Tomatoes", "Vegetables", 10),
        ("Oranges", "Fruits", 5)
    ]
    
    cur.executemany(insert_sql, values)
    myconn.commit()
    print("\n", cur.rowcount, "records inserted successfully.")
    myconn.close()
except Exception as e:
    print("Error:", e)

# 6. Fetch and Display All Table Items
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",
        database="pantry_db"
    )
    cur = myconn.cursor()
    cur.execute("SELECT * FROM pantry_items")
    result = cur.fetchall()
    
    print("\nAll Table Items:\n")
    for row in result:
        print(row)
    myconn.close()
except Exception as e:
    print("Error:", e)


# ==========================================
# Part 3: Exception Handling
# ==========================================

print("\n--- 1. Missing File Test ---")
try:
    file = open("missing.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found!")

print("\n--- 2. Text instead of Numbers Test ---")
try:
    quantity = int("abc")
    print("Quantity accepted:", quantity)
except ValueError:
    print("Error: 'abc' is not a valid number!")

print("\n--- 3. Database Connection Error Test ---")
try:
    myconn = sql.connect(
        host="localhost",
        user="root",
        password="wrong_password",
        database="pantry_db"
    )
    myconn.close()
except sql.Error as err:
    print("Database connection error:", err)

print("\n--- 4. Empty Fields Test ---")
try:
    item_name = ""
    if item_name == "":
        raise Exception("Item name cannot be empty!")
    print("Item name:", item_name)
except Exception as e:
    print("Error:", e)

print("\n--- 5. Multiple Exceptions Test ---")
try:
    result = 100 / 0
    print("Result:", result)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

print("\n--- 6. Finally Clause Test ---")
file = None
try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: test.txt not found!")
finally:
    if file:
        file.close()
        print("File closed in finally block")
    else:
        print("Finally block executed (no file to close)")


# ==========================================
# Part 4: Advanced Database Operations 
# ==========================================

    myconn = sql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",
        database="pantry_db"
    )
    cur = myconn.cursor()

    # 1. Add New Column
    print("\nAdding new column")
    try:
        cur.execute("ALTER TABLE pantry_items ADD COLUMN ExpDate DECIMAL(10,2) DEFAULT 0")
        myconn.commit()
        print("Column 'ExpDate' added successfully!")
    except Exception as e:
        print("Error adding column:", e)

    # 2. View All Items
    print("\n--- 2. Viewing all items ---")
    cur.execute("SELECT * FROM pantry_items")
    results = cur.fetchall()
    print("All Table Items:")
    for row in results:
        print(row)

    # 3. Search for Items Starting with 'R'
    print("\n--- 3. Searching for items starting with 'R' ---")
    cur.execute("SELECT * FROM pantry_items WHERE item_name LIKE 'R%'")
    results = cur.fetchall()
    if len(results) == 0:
        print("No items found starting with 'R'")
    else:
        for row in results:
            print(row)

    # 4. Add One New Row
    print("\n--- 4. Adding one new row ---")
    cur.execute("INSERT INTO pantry_items (item_name, category, quantity) VALUES ('New Item', 'New Category', 1)")
    myconn.commit()
    print("New row added successfully!")

    # 5. Delete an Item
    print("\n--- 5. Deleting an item ---")
    cur.execute("DELETE FROM pantry_items WHERE id = 11")
    myconn.commit()
    if cur.rowcount > 0:
        print("Item deleted successfully!")
    else:
        print("No item found with ID 11")

    # 6. Exit / Final Table
    print("\n--- 6. Exit program ---")
    print("Thank you for using Smart Home Pantry Manager!")
    
    print("\n--- Final Table ---")
    cur.execute("SELECT * FROM pantry_items")
    final = cur.fetchall()
    for row in final:
        print(row)

    myconn.close()
