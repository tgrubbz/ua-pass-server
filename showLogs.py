import sqlite3

conn = sqlite3.connect('pass.db')

cur = conn.execute('SELECT * FROM Logs')

print 'Id, Plate, Timestamp, Access'
for row in cur:
    show = ''
    for col in row:
        show += str(col) + ', '
    print show

