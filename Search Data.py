import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
        select name, brand, model from TBCars
        where
            id = 101
    """)
print(k.fetchall())

koneksi_ke_DB.close()
