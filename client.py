import socket
from configuration import config

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = config['host']
port = config['port']
s.connect((host , port))

while True:
    msg = s.recv(1024)
    print(msg)