import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)



jeff = face_recognition.load_image_file("jeffbezos.JPG")
jeff_encoding = face_recognition.face_locations(jeff)[0]

