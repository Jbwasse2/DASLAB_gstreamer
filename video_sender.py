import numpy as np
import cv2

framerate = 25

out = cv2.VideoWriter('appsrc ! videoconvert ! '
                      'x264enc noise-reduction=10000 speed-preset=ultrafast tune=zerolatency ! '
                      'rtph264pay config-interval=1 pt=96 !'
                      'tcpserversink host=127.0.0.1 port=6002 sync=false',
                      0, framerate, (640, 480))

cap = cv2.VideoCapture("Dog.mp4")

while(True):
    ret, frame = cap.read()
    if ret:
#        print("got frame")
        out.write(frame)
cap.release()
cv2.destroyAllWindows()
