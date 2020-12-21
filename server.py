import socket

HOST = '127.0.0.1'
PORT = 65432


word_dict = {'emission': 'Get out', 'Notemission': 'Stay'}


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            method, word = data.split()
            if word not in word_dict:
                conn.sendall(bytes("ERROR Word not found", "utf-8"))
                break
            word_definition = word_dict[word]

            if not data:
                conn.sendall(bytes("ERROR Word not found", "utf-8"))
                break
            conn.sendall(bytes(f"ANSWER {word_definition}", "utf-8"))
