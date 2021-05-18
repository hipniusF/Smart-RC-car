import socket
import os

import cv2
import numpy as np

from helpers.config import config
from helpers.config import address

class Client(socket.socket):
    def __init__(self, address=(address)):
        super(Client, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address

    def connect(self):
        super().connect(self.address)

    def get_data(self):
        while True:
            yield super().recv(921600)
