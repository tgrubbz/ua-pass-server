import sqlite3

def connect():
    return sqlite3.connect('pass.db', detect_types = sqlite3.PARSE_DECLTYPES)

def exists(table):
    conn = connect()
    cur = conn.execute('''
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name=?''', (table,))
    return cur.fetchone() != None
    

def createLogTable():
    conn = connect()
    conn.execute('''
        CREATE TABLE Logs
        (
            Id          INTEGER PRIMARY KEY AUTOINCREMENT,
            Plate       TEXT                NOT NULL,
            Timestamp   TEXT                NOT NULL,
            Access      BIT                 NOT NULL
        );''')

def createUserTable():
    conn = connect()
    conn.execute('''
        CREATE TABLE Users
        (
            Id          INTEGER PRIMARY KEY AUTOINCREMENT,
            Plate       TEXT    UNIQUE      NOT NULL,
            Timestamp   TEXT                NOT NULL,
            Access      BIT                 NOT NULL
        );''')

def addLog(log):
    if not exists('Logs'):
        createLogTable()

    conn = connect()
    cur = conn.execute('''
        INSERT INTO Logs
        (Plate, Timestamp, Access)
        VALUES
        (:plate, :timestamp, :access)
        ''', log)
    conn.commit()
    print 'Logs added: ', cur.rowcount
    return cur.rowcount
    


        
    

    

    
    
    
