import os 

os.system('pip install --upgrade pip')
os.system('pip install wheel')
os.system('pip install twine')
os.system('pip install numpy')
os.system('pip install python3-opencv')
os.system('python example_project/setup.py sdist bdist_wheel')
os.system('twine upload dist/*')

import cv2
import time

video = cv2.VideoCapture(0)
faceclassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ImageRead, image = video.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    faces = faceclassifier.detectMultiScale(gray, 1.3, 5)
    for(fx, fy, fw, fh) in faces:
        cv2.rectangle(image, (fx, fy), ())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
