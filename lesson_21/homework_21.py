import sqlite3

conn = sqlite3.connect('SQLLite_DB')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
    id number NUT NULL,
    categories_name TEXT NOT NULL,
    description TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    product_name TEXT NOT NULL,
    price number NOT NULL,
    category_id number NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id))''')

categories_insert_data = [
    (1, 'PC hardware', 'All what you need to build a PC'),
    (2, 'Major Appliances', 'Home appliances'),
    (3, 'Games', 'Games for PC and all types of consoles')]

products_insert_data = [
    ('NVIDIA 5070 TI', 800, 1),
    ('LG GBP62PZNBC', 900, 2),
    ('SAMSUNG DV90DG52A0ABLE', 600, 2),
    ('NVIDIA 5060', 500, 1),
    ('NVIDIA 5090 TI', 1500, 1),
    ('RYZEN 9900X3D', 600, 1),
    ('STALKER 2', 70, 3),
    ('ARC Raiders', 70, 3),
    ]

cursor.executemany(f'''INSERT INTO categories (id, categories_name, description) VALUES (?, ?, ?)''', categories_insert_data)
cursor.executemany(f'''INSERT INTO products (product_name, price, category_id) VALUES (?, ?, ?)''', products_insert_data)

conn.commit()

