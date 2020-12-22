import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


word_dict = {'emission': 'Get out', 'Notemission': 'Stay'}

def handle_client(conn, addr):
    with conn:
        print('Connected to', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            try:
                method, word = data.split()
            except:
                if data == "STOP":
                    conn.sendall(bytes("STOP Server stopped", "utf-8"))
                    break
                conn.sendall(bytes("ERROR Something happened", "utf-8"))
                break

            if method == "GET":
                if word not in word_dict:
                    conn.sendall(bytes("ERROR Word not found, try again.", "utf-8"))
                    continue
                conn.sendall(bytes(f"ANSWER {word_dict[word]}", "utf-8"))
            else:
                conn.sendall(bytes("ERROR Method not recognized.", "utf-8"))
                break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening...')
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
