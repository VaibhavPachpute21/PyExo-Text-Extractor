import pytesseract
import cv2
import os
import re
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

path = os.getcwd()+"\\src\\test"

voterList = ['voter.jpg','voter1.jpg','voter2.jpg','voter3.jpg','voter4.jpg']
allFiles = os.listdir(path)

for file in voterList:
    imPath = path+'\\'+file
    # print(imPath)
    filePath = os.getcwd()+'\\src\\extracts\\%s_voter.txt'%file
    image = cv2.imread(imPath)
    text = pytesseract.image_to_string(image, lang='eng+hin+mar')
    

    if str(text).__contains__('ELECTION'):
        if str(text).__contains__('Elector') or str(text).__contains__("Eléctor's") or str(text).__contains__("Elector's") or str(text).__contains__("Elector's Name"):
            print("HI")
            print()
            """ full_name = str(text).split('Elector')[1] """
            """ print(full_name) """
            print(str(text).split('Elector'))
            print('\n')
            print('\n')


        with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text).replace('\t', '').replace('\n\n', '\n'))
    else:
        # print(str(text))
        # print("didn't found: ", imPath)
        pass
