import mysql.connector

mydb = mysql.connector.connect(
    host='##########',
    user='##########',
    password='##########',
    database='##########'
)

#print(mydb)

#mycursor = mydb.cursor()
# #mycursor.execute("CREATE DATABASE mydatabase")
# # mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
#
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
#
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#
# Insert a record
# sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mydb.commit()
# print(mycursor.rowcount, "record inserted")
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql,val)
# mydb.commit()
# print("1 record inserted, ID: ", mycursor.lastrowid)
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#
# #all rows
#
# mycursor.execute("SELECT address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


#one row

# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)

# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
# mycursor.execute(sql)
# myresult  =mycursor.fetchall()
# for x in myresult:
#     print(x)


# mycursor = mydb.cursor()
#
# sql = "SELECT * FROM customers WHERE address Like '%way%'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


#Prevent SQL injections
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2",)
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#Sort the result
#Ascending
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Descending

# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# DELETE any record

# mycursor = mydb.cursor()
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit() # Important
# print(mycursor.rowcount, "record(s) deleted")

# mycursor = mydb.cursor()
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2",)
# mycursor.execute(sql, adr)
# mydb.commit() # Important
# print(mycursor.rowcount, "record(s) deleted")


mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE seller (name VARCHAR(255), address VARCHAR(255))")
#
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# sql = "INSERT INTO seller(name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mydb.commit()
# print(mycursor.rowcount, "record inserted")
#
#
# sql = "INSERT INTO seller (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

# mycursor=mydb.cursor()
# sql="DROP TABLE seller"
# mycursor.execute(sql)

# mycursor=mydb.cursor()
# sql="DROP TABLE IF EXISTS seller"
# mycursor.execute(sql)

# Update table

# mycursor=mydb.cursor()
# sql = "UPDATE customers SET address ='Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# mycursor=mydb.cursor()
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# mycursor=mydb.cursor()
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor=mydb.cursor()
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


#Join two or more tables

#mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE user (name VARCHAR(255), fav VARCHAR(255))")
#
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

#mycursor.execute("ALTER TABLE user ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# sql = "INSERT INTO user (name, fav) VALUES (%s, %s)"
# val = [
#   ('John', '154'),
#   ('Peter', '154'),
#   ('Hannah', 'Mountain 21'),
#   ('Amy', '155'),
#   ('Hannah','' ),
#   ('BMichael', ''),
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")




# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE products (name VARCHAR(255))")
#
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# mycursor.execute("ALTER TABLE products ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [
#   ('154', 'Chocolate Heaven'),
#   ('155', 'Tasty Lemons'),
#   ('156', 'Vanilla Dreams')
#
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")


# mycursor.execute("SELECT * FROM products ")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# mycursor=mydb.cursor()
#
# sql = "SELECT \
#   user.name AS user, \
#   products.name AS favorite \
#   FROM user \
#   INNER JOIN products ON user.fav = products.id"
#
# mycursor.execute(sql)
# myresult  = mycursor.fetchall()
# for x in myresult:
#     print(x)


#Left join
# mycursor=mydb.cursor()
#
# sql = "SELECT \
#   user.name AS user, \
#   products.name AS favorite \
#   FROM user \
#   LEFT JOIN products ON user.fav = products.id"
#
# mycursor.execute(sql)
# myresult  = mycursor.fetchall()
# for x in myresult:
#     print(x)

#Right join

mycursor=mydb.cursor()

sql = "SELECT \
  user.name AS user, \
  products.name AS favorite \
  FROM user \
  RIGHT JOIN products ON user.fav = products.id"

mycursor.execute(sql)
myresult  = mycursor.fetchall()
for x in myresult:
    print(x)





