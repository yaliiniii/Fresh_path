import sqlite3
import os

db_path = "./freshpath.db"
if os.path.exists(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Drop tables to force recreation
        cursor.execute("DROP TABLE IF EXISTS habits")
        cursor.execute("DROP TABLE IF EXISTS habit_definitions")
        
        conn.commit()
        print("Tables dropped successfully")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Database not found")
