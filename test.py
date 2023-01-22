import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import pytesseract
import table_ocr as tb
import re
from keras.models import load_model

file = os.getcwd()+"\\src\\test\\voter.jpg"
# file='D:\Web\eCell\src\\test\pan-card.jpg'
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'



image=cv2.imread(file)
# Load the model
model = load_model('./src/model/keras_model.h5',compile=False)

# CAMERA can be 0 or 1 based on default camera of your computer.
# camera = cv2.VideoCapture(0)

# Grab the labels from the labels.txt file. This will be used later.
labels = open('./src/model/labels.txt', 'r').readlines()

# while True:
# Grab the webcameras image.
# ret, image = camera.read()
# Resize the raw image into (224-height,224-width) pixels.
image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
# Show the image in a window
cv2.imshow('Webcam Image', image)
cv2.waitKey(0)
# Make the image a numpy array and reshape it to the models input shape.
image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
# Normalize the image array
image = (image / 127.5) - 1
# Have the model predict what the current image is. Model.predict
# returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
# it is the first label and 80% sure its the second label.
probabilities = model.predict(image)
# Print what the highest value probabilitie label
print(labels[np.argmax(probabilities)].split(' ')[1])
# Listen to the keyboard for presses.

