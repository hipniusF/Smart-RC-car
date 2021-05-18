import cv2

from eyes import VideoClient
from link import Client

video_client = VideoClient()
video_client.connect()

for frame in video_client.get_data():
    cv2.imshow('a', frame)
    cv2.waitKey(1)
