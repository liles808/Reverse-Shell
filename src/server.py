import socket
import sys

# Create socket
def sc_create():
    try:
        global s
        s = socket.socket();
        print("Socket created.")
    except socket.error as msg:
        print("Socket creation error: "+str(msg))

# Bind socket to a port
def sc_bind():
    try:
        host = ''
        port = 9997
        s.bind((host, port))
        s.listen(5)
        print("Socket binding to port...")
    except socket.error as msg:
        print("Socket bind error: "+str(msg))
        sc_bind()

# Socket accepts connections
def accept_conn():
    conn, address = s.accept()
    print("Connection established with" + address[0])
    cmd_exe()

# Send commands to client
def cmd_exe():
    cmd = input();
    if cmd == 'exit':
        conn.close()
        s.close()
        sys.exit()
    else:
        conn.send(str.encode(input))
        response = str(conn.recv(1024), "utf-8")
        print(response)

# Main execution method
def main():
    sc_create()
    sc_bind()
    accept_conn()

main()
