from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import sqlite3

app = FastAPI()


conn = sqlite3.connect("north_pole.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS elves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        free BOOLEAN,
        maternity_leave BOOLEAN
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS packages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        elf_id INTEGER,
        FOREIGN KEY (elf_id) REFERENCES elves (id)
    )
''')
conn.commit()
conn.close()
