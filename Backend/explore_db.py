#!/usr/bin/env python3
import sqlite3
import json
from datetime import datetime

def explore_database():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    
    print("=== SQLITE DATABASE EXPLORER ===\n")
    
    # Show tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {[table[0] for table in tables]}\n")
    
    # Show notes table structure
    cursor.execute("PRAGMA table_info(notes);")
    columns = cursor.fetchall()
    print("Notes table structure:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
    print()
    
    # Show all notes
    cursor.execute("SELECT * FROM notes;")
    notes = cursor.fetchall()
    print(f"Total notes: {len(notes)}\n")
    
    for note in notes:
        print(f"ID: {note[0]}")
        print(f"Title: {note[1]}")
        print(f"Content: {note[2][:50]}...")
        print(f"Tags: {note[3]}")
        print(f"Created: {note[4]}")
        print(f"Updated: {note[5]}")
        print(f"Archived: {note[6]}")
        print("-" * 40)
    
    conn.close()

if __name__ == "__main__":
    explore_database()