import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import pytesseract
import table_ocr as tb
file = os.getcwd()+"\\src\\test\\passport1.jpg"

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

image=cv2.imread(file)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO)
cv2.imshow("",thresh1)
cv2.waitKey(0)

text = pytesseract.image_to_string(thresh1, lang='eng+hin+mar')
print(str(text))


filePath = os.getcwd()+'\\src\\extracts\\pass.txt'
with open(filePath, 'w', encoding="utf-8") as f:
    f.write(str(text))


# fpath='D:\Web\eCell\src\extracts\detecttable_statement.csv'
# with open(fpath, "r", encoding="utf-8") as file:
#                 string = file.read()
#                 newArr=string.split('\n')
#                 for row in newArr:
#                     if ("Date" in row):
#                         spliter=row
#                         if ("Balance" in spliter):

#                             formData=spliter.replace(' ',',')+ string.split(spliter)[1].replace(' ',',')
#                             print(formData)
#                             filePath = os.getcwd()+'\\src\\extracts\\testtt_statement.csv'
#                             with open(filePath, 'w', encoding="utf-8") as f:
#                                 f.write(formData)



# file = 'src/test/bank1.jpg_statement.csv'
# print(file.split('/')[-1].split('.')[0])


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
