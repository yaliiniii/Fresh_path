import sqlite3
import os

db_path = "./freshpath.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("--- Habits Table ---")
    cursor.execute("PRAGMA table_info(habits)")
    for col in cursor.fetchall():
        print(col)
        
    print("\n--- Habit Definitions Table ---")
    cursor.execute("PRAGMA table_info(habit_definitions)")
    for col in cursor.fetchall():
        print(col)
        
    conn.close()
else:
    print("Database not found")
