import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import pytesseract
import table_ocr as tb
import re

file = os.getcwd()+"\\src\\test\\passport.jpg"
# file='D:\Web\eCell\src\\test\pan-card.jpg'
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

# image=cv2.imread(file)
# image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# ret,thresh1 = cv2.threshold(image,100,255,cv2.THRESH_BINARY)

# titles = ['Original Image', 'Binary Thresholding']
# images = [image, thresh1]
# for i in range(2):
#     plt.figure(figsize=(20,20))
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# cv2.imshow("",image)
# cv2.waitKey(0)
# text = pytesseract.image_to_string(image, lang='eng+hin+mar')

filePath = os.getcwd()+'\\src\\extracts\\passport.txt'
# with open(filePath, 'w', encoding="utf-8") as f:
#     f.write(str(text))


with open(filePath, "r", encoding="utf-8") as file:

    string = file.read().strip()
    stringArr=string.split('\n')
    dt=re.findall(r'\d{2}/\d{2}/\d{4}', string)
    lastLine=stringArr[-1]
    slastLine=stringArr[-2]
    print("passportNo:",lastLine.split('<')[0])
    print("Type:",slastLine.split('<')[0])
    print("Nationality:",slastLine.split('<')[1][0:3])
    print("First Name:",slastLine.split('<')[3])
    print("Last Name:",slastLine.split('<')[1].replace(slastLine.split('<')[1][0:3],''))
    print("DOB:",dt[0])
    print("Date of issue:",dt[1])
    print("Date of Expiry:",dt[2])
    

    



""" 
voterList = ['voter.jpg','voter1.jpg','voter2.jpg','voter3.jpg','voter4.jpg']
allFiles = os.listdir(path)

voterArr=[]
for file in voterList:
    imPath = path+'\\'+file
    # print(imPath)
    filePath = os.getcwd()+'\\src\\extracts\\%s_voter.txt'%file
    image = cv2.imread(imPath)
    kernel=np.array([[-1,-1,-1], [-1,5,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    cv2.imshow("sharp",sharpened)
    cv2.waitKey(0)
    text = pytesseract.image_to_string(sharpened, lang='eng+hin+mar')

    with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(text).replace('\t', '').replace('\n\n', '\n'))
    
    print(text)
    if str(text).__contains__('ELECTION'):
        electors_Name=''
        father_name=''
        husband_name=''
        gender=''

        newArr=str(text).split('\n')
        for i in newArr:
            if ("Elector") in i :
                electors_Name= i.split('Name')[1].replace(":","").strip()
            if ("Eléctor") in i:
                electors_Name= i.split('Name')[1].replace(":","").strip()
            if ("Father") in i:
                father_name= i.split('Name')[1].replace(":","").strip()
            if ("Husband") in i:
                husband_name=i.split('Name')[1].replace(":","").strip()
            if "Male" in i:
                gender="Male"
            if "Female" in i:
                gender="Female"

        voterObj={
            "Name:": electors_Name,
            "Father Name:":father_name,
            "Husband Name:":husband_name,
            "Gender:":gender
        }
        voterArr.append(voterObj)
            
        with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text).replace('\t', '').replace('\n\n', '\n'))
    else:
        # print(str(text))
        # print("didn't found: ", imPath)
        pass
print(voterArr) """

import cv2
import numpy as np
from keras.models import load_model

# Load the model
model = load_model('keras_model.h5')

# CAMERA can be 0 or 1 based on default camera of your computer.
camera = cv2.VideoCapture(0)

# Grab the labels from the labels.txt file. This will be used later.
labels = open('labels.txt', 'r').readlines()

while True:
    # Grab the webcameras image.
    ret, image = camera.read()
    # Resize the raw image into (224-height,224-width) pixels.
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    # Show the image in a window
    cv2.imshow('Webcam Image', image)
    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    # Normalize the image array
    image = (image / 127.5) - 1
    # Have the model predict what the current image is. Model.predict
    # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
    # it is the first label and 80% sure its the second label.
    probabilities = model.predict(image)
    # Print what the highest value probabilitie label
    print(labels[np.argmax(probabilities)])
    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)
    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
