import sqlite3

def list_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

def fetch_table_data(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    conn.close()
    return column_names, rows

def print_db_contents(db_path):
    tables = list_tables(db_path)
    print(f"Tables in database '{db_path}':")
    for table in tables:
        print(f"\nTable: {table}")
        column_names, rows = fetch_table_data(db_path, table)
        print("Columns:", column_names)
        for row in rows:
            print(row)

# Replace 'example.db' with the path to your actual database file
db_path = 'sqlite.db'
print_db_contents(db_path)
