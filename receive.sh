#!/usr/bin/env bash
#

while true
do
gst-launch-1.0 -v udpsrc port=6002 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! autovideosink
done
