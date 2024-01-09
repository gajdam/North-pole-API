from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

conn = sqlite3.connect('north_pole.db')
cursor = conn.cursor()


@app.get("/parcels")
async def get_all_parcels():
    create_parcels_table()

    result = cursor.execute("SELECT * FROM parcels")
    data = result.fetchall()
    conn.commit()

    if data:
        return {"message": data}
    else:
        raise HTTPException(status_code=404, detail="No parcels available")


@app.get("/elves/all")
async def get_all_elves():
    create_elves_table()

    result = cursor.execute("SELECT * FROM elves")
    data = result.fetchall()
    conn.commit()

    if data:
        return {"message": data}
    else:
        raise HTTPException(status_code=404, detail="No elves available")


def create_parcels_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parcels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            elfID INTEGER,
            name TEXT,
            status INTEGER DEFAULT 0
        )''')


def create_elves_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS elves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            vacation INTEGER DEFAULT 0,
            daternity INTEGER DEFAULT 0
        )''')


@app.post("/parcel")
async def post_parcel(name: str, elfID: int):
    create_parcels_table()

    cursor.execute('INSERT INTO parcels (elfID, name) VALUES (?, ?)', (elfID, name))
    conn.commit()
    return {"message": "Parcel added successfully"}


@app.put("/parcel")
async def put_parcel(parcel_id: int, status: bool):
    create_parcels_table()

    cursor.execute('UPDATE parcels SET status = ? WHERE id = ?', (int(status), parcel_id))
    conn.commit()
    return {"message": "Parcel status updated successfully"}


@app.get("/parcel")
async def get_parcel(parcel_id: int):
    create_parcels_table()

    result = cursor.execute("SELECT * FROM parcels WHERE id = ?", (parcel_id,))
    data = result.fetchall()
    conn.commit()

    if data:
        return {"message": data}
    else:
        raise HTTPException(status_code=404, detail="No parcel with that ID")


@app.delete("/parcels/{parcel_id}")
async def delete_parcel(parcel_id: int):
    create_parcels_table()

    cursor.execute("DELETE FROM parcels WHERE id = ?", (parcel_id,))
    conn.commit()
    return {"message": f"Parcel with ID {parcel_id} successfully deleted"}


@app.post("/elves")
async def post_elf(elf_name: str):
    create_elves_table()

    cursor.execute('INSERT INTO elves (name) VALUES (?)', (elf_name,))
    conn.commit()
    return {"message": "Elf added successfully"}


@app.put("/elves")
async def put_elf(elfID: int, vacation: bool, daternity: bool):
    create_elves_table()

    cursor.execute('UPDATE elves SET vacation = ?, daternity = ? WHERE id = ?', (int(vacation), int(daternity), elfID))
    conn.commit()
    return {"message": "Elf information updated successfully"}


@app.get("/elves")
async def get_elf(elfID: int):
    create_elves_table()

    result = cursor.execute("SELECT * FROM elves WHERE id = ?", (elfID,))
    data = result.fetchall()
    conn.commit()

    if data:
        return {"message": data}
    else:
        raise HTTPException(status_code=404, detail="No elf with that ID")


@app.delete("/elves")
async def delete_elf(elfID: int):
    create_elves_table()

    cursor.execute("DELETE FROM elves WHERE id = ?", (elfID,))
    conn.commit()
    return {"message": "Elf successfully fired"}
