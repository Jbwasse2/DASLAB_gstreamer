import numpy as np
import cv2
from multiprocessing import Process
import time

framerate = 25
def send():

    cap_send = cv2.VideoCapture("v4l2src ! video/x-raw,format=BGR,width=640,height=480,framerate=30/1 ! appsink,CAP_GSTREAMER");
    cap_send = cv2.VideoCapture(0);
    out_send = cv2.VideoWriter("appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000",0,30,(640,480))

    out_send = cv2.VideoWriter('appsrc ! videoconvert ! '
                      'x264enc noise-reduction=10000 speed-preset=ultrafast tune=zerolatency ! '
                      'rtph264pay config-interval=1 pt=96 !'
                      'tcpserversink host=127.0.0.1 port=5000 sync=false',
                      0, framerate, (640, 480))

    if not out_send.isOpened():
        print("VideoCapture not opened!")
        exit(0)
    if not cap_send.isOpened():
        print('VideoWriter not opened')
        exit(0)

    while True:
        ret,frame = cap_send.read()

        if not ret:
            print('empty frame')
            break

        out_send.write(frame)

        cv2.imshow('send', frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break

    cap_send.release()
    out_send.release()

def receive():
    cap_receive = cv2.VideoCapture("udpsrc port=5000 ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink");

    if not cap_receive.isOpened():
        print('VideoCapture not opened')
        exit(0)

    while True:
        ret,frame = cap_receive.read()

        if not ret:
            print('empty frame')
            break

        cv2.imshow('receive', frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break

    cap_receive.release()

if __name__ == '__main__':
    r = Process(target=receive)
    s = Process(target=send)
    r.start()
    s.start()
    s.join()
    r.join()

    cv2.destroyAllWindows()
