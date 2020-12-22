import socket
import threading

class Server:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 65432
        self.word_dict = {'emission': 'Get out', 'Notemission': 'Stay'}

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))

    def connect(self):
        self.socket.listen()
        while True:
            conn, addr = self.socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        while True:
            data = conn.recv(1024).decode('UTF-8').strip()
            try:
                method, word = data.split(' ', 1)
            except:
                if data == "STOP":
                    conn.sendall("STOP Server stopped\n".encode())
                    break
                conn.sendall("ERROR Something happened\n".encode())
                break

            if method == "GET":
                if word not in self.word_dict:
                    conn.sendall("ERROR Word not found, try again\n".encode())
                    continue
                conn.sendall(f"ANSWER {self.word_dict[word]}\n".encode())
            else:
                conn.sendall("ERROR Method not recognized\n".encode())
                break

if __name__ == '__main__':
    Server().connect()
