#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cv2


class ImageProcess:

    @staticmethod
    def detect_face(filename: str):
        print('ImageProcess.detect_face:', filename)
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        # cv2.imshow(filename, image)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.3,
                                              minNeighbors=5)
        for x, y, w, h in faces:
            print(f'face(x={x}, y={y}, w={w}, h={h})')
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face = image[y:y+h, x:x+w]
            face = cv2.resize(face, (w // 30, h // 30))
            face = cv2.resize(face, (w, h), interpolation=cv2.INTER_AREA)
            image[y:y+h, x:x+w] = face

        cv2.imwrite(filename, image)
