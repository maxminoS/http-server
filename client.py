import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        inp = input('Enter: ')
        s.sendall(bytes(inp, 'utf-8'))
        data = s.recv(1024).decode('utf-8')
        method = data.split()[0]
        print(data)
        if method == "ERROR" or method == "STOP":
            break
