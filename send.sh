#!/usr/bin/env bash
#

while true
do
gst-launch-1.0 -v filesrc location=Dog.mp4 ! decodebin ! x264enc ! rtph264pay ! udpsink host=127.0.0.1 port=6002
done
