import sqlite3

def fetch_data_by_id(db_path, table_name, record_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (record_id,))
    row = cursor.fetchone()
    column_names = [description[0] for description in cursor.description]
    conn.close()
    return column_names, row

def print_record_by_id(db_path, table_name, record_id):
    column_names, row = fetch_data_by_id(db_path, table_name, record_id)
    if row:
        print("Record found:")
        for col_name, value in zip(column_names, row):
            print(f"{col_name}: {value}")
    else:
        print("No record found with that ID.")

# Replace 'example.db' and 'your_table' with your actual database path and table name
db_path = 'sqlite.db'
table_name = 'Task'  # Replace with the actual table name you want to search

# Input ID
record_id = input("Enter the ID to search: ").strip()
print_record_by_id(db_path, table_name, record_id)
