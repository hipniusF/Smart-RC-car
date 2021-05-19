import numpy as np

from link import Client
from helpers.config import video_address

class VideoClient(Client):
    def __init__(self):
        super(VideoClient, self).__init__(video_address)

    def get_data(self):
        data = b''
        while True:
            new_data = super().recv(921600)
            if len(data) < 921600:
                data += new_data

            if len(data) >= 921600:
                frame = np.frombuffer(data[:921600], dtype=np.uint8)
                frame = frame.reshape(480, 640, 3)

                data = data[921600:]
                yield frame
