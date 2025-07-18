import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
        insert into TBCars(
            id,
            name,
            brand,
            model,
            price
        )
        values(
            '101',
            'Red Car',
            'Honda',
            'CRV',
            12000
        )
        """)

koneksi_ke_DB.commit()
koneksi_ke_DB.close()