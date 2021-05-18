from time import sleep
import numpy as np
import socket
import cv2

from link import Server

class VideoServer(Server):
    def __init__(self):
        super(VideoServer, self).__init__(5005)

    def msg_handler(self, client):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            data = frame.tobytes()
            client.sendall(data)

            cv2.waitKey(1)
