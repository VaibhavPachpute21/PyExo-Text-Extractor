import pytesseract
import cv2
import os
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'
image=cv2.imread('D:\Web\eCell\src\\test\pan1.jpg')

text = pytesseract.image_to_string(image, lang='eng+hin+mar')
print(text)


if str(text).__contains__('Permanent Account Number'):
    PanNO=str(text).split('Number')[1].split('\n')[1]
    filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt'%PanNO
    with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text).replace('\t','').replace('\n\n','\n'))
else:
    print("didn't found") 