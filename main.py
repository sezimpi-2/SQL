import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products (
        product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def change_quantity_products(conn, change_quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, change_quantity)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_price_products(conn, change_price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, change_price)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, delete_id):
    try:
        sql = '''DELETE FROM PRODUCTS SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (delete_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def select_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_order_by_price(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def find_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)




sql_create_products_table = '''
CREATE TABLE products
(id integer PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER (8) NOT NULL DEFAULT 0)'''


connection = create_connection("hw.db")
if connection is not None:
    print("Connected Succes")
    create_table(connection, sql_create_products_table)
    create_product(connection, ('Жидкое мыло', 63.76, 4))
    create_product(connection, ('Твердое мыло', 44.56, 45))
    create_product(connection, ('мыло', 61.56, 67))
    create_product(connection, ('bread', 45.60, 6))
    create_product(connection, ('coke', 56.60, 6))
    create_product(connection, ('water', 78.60, 5))
    create_product(connection, ('air', 66.60, 4))
    create_product(connection, ('iphone', 5.60, 1))
    create_product(connection, ('samsung', 60.60, 3))
    create_product(connection, ('Hyenday', 3.60, 5))
    create_product(connection, ('bmw', 6.60, 9))
    create_product(connection, ('mercedes', 1.60, 6))
    create_product(connection, ('audi', 30.60, 7))
    create_product(connection, ('lexus', 4.60, 8))
    create_product(connection, ('macbook', 43.60, 3))
    create_product(connection, ('lenovo', 45.60, 4))
    change_quantity_products(connection, (50, 1))
    change_price_products(connection, (250, 2))
    delete_products(connection, 2)
    select_products(connection)
    select_products_order_by_price(connection)
    find_by_word(connection, "Мыло")
