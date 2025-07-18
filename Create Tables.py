import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
        CREATE TABLE IF NOT EXISTS TBCars(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            price REAL NOT NULL
        )
        """)

koneksi_ke_DB.commit()
koneksi_ke_DB.close()