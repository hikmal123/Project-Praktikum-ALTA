import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
        delete from TBCars
        where
            id = 101
    """)

koneksi_ke_DB.commit()
koneksi_ke_DB.close()