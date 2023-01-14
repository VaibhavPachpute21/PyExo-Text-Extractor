import pytesseract
import cv2
import os
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

image=cv2.imread('./src/test/pan1.jpg')

# image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("pan",image)
cv2.waitKey(0)

text=pytesseract.image_to_string(image,lang='eng+hin+mar')

if str(text).__contains__('Permanent Account Number'):
    PanNO=str(text).split('Number')[1].split('\n')[1]
    filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt'%PanNO
    with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text))
else:
    print("didn't found")