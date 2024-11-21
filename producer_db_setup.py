import sqlite3

# Change here for correct path if you need
PRODUCTS_DB_PATH = "C:\\Users\\vijis\\Kafka_proj\\sqlite_connect\\project_kafka.db"
PRODUCTS_FILE = "products.txt"

def producer_db_setup() -> sqlite3.Cursor:

    db = sqlite3.connect(PRODUCTS_DB_PATH)

    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS products 
                (productid INTEGER PRIMARY KEY AUTOINCREMENT,
                productname TEXT,
                type TEXT, 
                pricetype TEXT, 
                price INTEGER, 
                saldo INTEGER)""")

    if not cursor.execute("SELECT * FROM products").fetchall():
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            for prod in f:
                p = prod.strip().strip("(").strip(")").strip("\n").replace(" ","").split(',')
                cursor.execute(f"INSERT INTO products (productname, type, pricetype, price, saldo) VALUES({p[0]},{p[1]},{p[2]},{p[3]},{p[4]})")
                db.commit()

    return cursor