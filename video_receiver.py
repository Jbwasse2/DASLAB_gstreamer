import numpy as np
import cv2

#vp8 = "udpsrc port=6002 , application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96 ! rtph264depay ! decodebin ! videoconvert ! autovideosink"
vp8 = "udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink name=sink emit-signals=true sync=false max-buffers=1 drop=true" 

cap = cv2.VideoCapture(vp8, cv2.CAP_GSTREAMER)

while(True):
    
    ret, frame = cap.read()
    
    if ret:
        print("Got video")
        cv2.imshow('receiver',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
