import sqlite3

def create_and_populate_db(db_name, num_rows):
    cn = sqlite3.connect(db_name)
    c = cn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS mydata
                 (id INTEGER PRIMARY KEY, ho TEXT, ten_dem TEXT, ten TEXT)''')

    for i in range(num_rows):
        c.execute("INSERT INTO mydata (ho, ten_dem, ten) VALUES (?, ?, ?)", ('Hihi_'+str(i), 'Huhu_'+str(i), 'Haha_'+str(i)))

    cn.commit()
    cn.close()

create_and_populate_db('data_cua_thang.db', 1000000)