import pytesseract
import cv2
import os
import re
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

path = "D:\Web\eCell\src\\test"
allFiles = os.listdir(path)
print(allFiles)
for file in allFiles:
    imPath = path+'\\'+file
    # print(imPath)
    image = cv2.imread(imPath)
    text = pytesseract.image_to_string(image, lang='eng+hin+mar')
    # print(str(text))

    if str(text).__contains__('DRIVE' or 'DRIVING LICENCE'):
        driLicenceNo = re.search(r"\d{4}", str(text))
        filePath = os.getcwd()+'\\src\\extracts\\%s_drving.txt'%file
        with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text).replace('\t', '').replace('\n\n', '\n'))
    else:
        print("didn't found: ", imPath)
