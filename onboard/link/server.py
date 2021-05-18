import socket
from multiprocessing import Process

class Server(socket.socket):
    def __init__(self, port=5000):
        self.port = port
        self.address = '127.0.0.1'

        super(Server, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

    def msg_handler(self, client):
        while True:
            client.sendall(bytes('Test', 'utf8'))

    def msg_handler_wrapper(self, client):
        try:
            self.msg_handler(client)

        except ConnectionResetError:
            client.close()
            return

    def serve(self):
        self.bind((self.address, self.port))
        self.listen(5)
        print(f'Listening on `{self.address}:{self.port}`...')

        while True:
            new_client, _ = self.accept()
            if new_client:
                p = Process(target=self.msg_handler_wrapper, args=(new_client,))
                p.start()
