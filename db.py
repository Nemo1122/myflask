import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

# cur_data = cur.execute('SELECT USERNAME, PASSWORD FROM USER')

# sql = 'SELECT 1 FROM USER WHERE USERNAME=? AND PASSWORD=?'
sql = 'SELECT 1 FROM USER WHERE USERNAME=1 or 1=1 --  AND PASSWORD=123'
is_valid_user = cur.execute(sql, ()).fetchone()
# is_valid_user = cur.execute(sql, ('nemo', '1234')).fetchone()
print(is_valid_user)

conn.close()
