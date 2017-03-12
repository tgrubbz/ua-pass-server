import sys
import socket
import json
import database as db

debug = True

# Default host = this ip addr
# Arbitrary port
host = ''
port = 50007

# Create the socet
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to a host and port
s.bind((host, port))

# Returns the decoded request string
def getRequestString(conn):
    raw = conn.recv(2048)
    return raw.decode()

# Receive the request from the connection 
def receive(conn):
    while True:
        request = getRequestString(conn)
        if len(request) == 0:
            continue

        conn.sendall('success')
        data = json.loads(request)

        if 'log' in data:
            db.addLog(data['log'])
            
        if 'end' in data and data['end'] == True:
            return
        

def listen():
    # listen for one connection
    s.listen(1)
    conn, addr = s.accept()

    if debug:
        print 'connection accepted', addr

    # Try to parse a request from the connection
    try:
        if debug:
            print 'parsing request...'
            
        receive(conn)

        if debug:
            print 'parsing complete'
    except:
        print 'Error: ', sys.exc_info()[0]
        raise


def start():
    while True:
        listen()        

