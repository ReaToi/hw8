import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error:
        print(sqlite3.Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error :
        print(sqlite3.Error)


database = 'hw.db'

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) not null default 0.0,
quantity INTEGER(5) not null default 0
)
'''

def create_product(conn, product):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def select_all_product(conn):
    try:
        sql = '''select * from products '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error:
        print(sqlite3.Error)

def select_all_product_search(conn, price, quantity):
    try:
        sql = '''select * from products where price <= ? and  quantity >= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price, quantity))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error:
        print(sqlite3.Error)

def update_quantity(conn, product):
    try:
        sql = '''update products set quantity = ? where id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def update_price(conn, product):
    try:
        sql = '''update products set price = ? where id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def selection_of_a_specific_product(conn, select):
    try:
        sql = '''select * from products where product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (select,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error:
        print(sqlite3.Error)


connection = create_connection(database)
if connection is not None:
    # create_table(connection, sql_create_products_table)
    # create_product(connection, ('apple', 50.90, 100))
    # create_product(connection, ('apricot', 40.70, 100))
    # create_product(connection, ('peach', 70, 100))
    # create_product(connection, ('cherry', 150, 100))
    # create_product(connection, ('tomat', 80.50, 100))
    # create_product(connection, ('cucumber', 80.50, 100))
    # create_product(connection, ('strawberry', 200, 100))
    # create_product(connection, ('watermelon', 270.30, 100))
    # create_product(connection, ('grapefruit', 250, 100))
    # create_product(connection, ('qiwi', 250, 100))
    # create_product(connection, ('mango', 450, 100))
    # create_product(connection, ('banana', 150, 100))
    # create_product(connection, ('raspberries', 350, 100))
    # create_product(connection, ('grape', 250.60, 100))
    # create_product(connection, ('candy', 300.80, 100))
    select_all_product(connection)
    # select_all_product_search(connection, 80, 5)
    # update_price(connection, (50, 11))
    # update_quantity(connection, (20, 14))
    # delete_product(connection, (25))
    selection_of_a_specific_product(connection, ('banana'))
    print('Done')
    connection.close()


