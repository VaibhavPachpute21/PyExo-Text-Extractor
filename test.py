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

voterArr=[]
for file in voterList:
    imPath = path+'\\'+file
    # print(imPath)
    filePath = os.getcwd()+'\\src\\extracts\\%s_voter.txt'%file
    image = cv2.imread(imPath)
    text = pytesseract.image_to_string(image, lang='eng+hin+mar')
    

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
            
    else:
        # print(str(text))
        # print("didn't found: ", imPath)
        pass
print(voterArr)