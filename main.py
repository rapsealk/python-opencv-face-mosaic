#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cv2
import time

FILENAME = str(int(time.time())) + '.avi'
WIDTH = 1080
HEIGHT = 720

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

"""
codec = cv2.VideoWriter_fourcc(*'XVID') # MP4V 0x7634706d
out = cv2.VideoWriter(FILENAME, codec, 20.0, (WIDTH, HEIGHT))
"""

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
        print(f'face(x={x}, y={y}, w={w}, h={h})')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (w // 30, h // 30))
        face = cv2.resize(face, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y+h, x:x+w] = face

    cv2.imshow('frame', frame)
    # out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
