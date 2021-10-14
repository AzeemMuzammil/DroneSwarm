import os
from multiprocessing.connection import Listener, Client


class Receiver:

    def __init__(self, port: int):
        self.address = ('localhost', port)
        self.listener = None
        self.conn = None

    def connect(self):
        self.listener = Listener(self.address, authkey=b'password')
        self.conn = self.listener.accept()

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

        if self.listener is not None:
            self.listener.close()

    def receive_data(self):
        if self.conn is not None:
            while True:
                msg = self.conn.recv()
                print(msg)
        else:
            print("There is no communication established to receive data")


class Sender:
    def __init__(self, port: int):
        self.address = ('localhost', port)
        self.conn = None

    def connect(self):
        self.conn = Client(self.address, authkey=b'password')

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def send_data(self, data: str):
        self.conn.send(data)
