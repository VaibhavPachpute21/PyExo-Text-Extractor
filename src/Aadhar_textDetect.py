import pytesseract
import cv2
import os
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'


class ExtractData():
    def __init__(self, file):
        self.file = file
        image = cv2.imread(file)
        text = pytesseract.image_to_string(image, lang='eng+hin+mar')
        string = str(text)
         #for Aadhar Card
        if string.__contains__('आधार - आदमी का अधकिर'):
            print(string)
            filePath = os.getcwd()+'\\src\\extracts\\_aadhar.txt'
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(string.replace('\t', '').replace('\n\n', '\n'))

        elif string.__contains__('मेरा आधार, मेरी पहचान'):
         match2 = re.search(r"\d{4}\s\d{4}\s\d{4}", string).group(0)
         print(match2)
         filePath = os.getcwd()+'\\src\\extracts\\%s_aadhar.txt'%match2
         with open(filePath, "w", encoding="utf-8") as file:
            file.write(string.replace('\t', '').replace('\n\n', '\n'))

        elif ("आधार - सामान्य माणसाचा अधिकार" in string):
            filePath = os.getcwd()+'\\src\\extracts\\%match2.group(0)'
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(string.replace('\t', '').replace('\n\n', '\n'))
        
        #for Pan Card
        elif string.__contains__('Permanent Account Number'):
         PanNO=str(text).split('Number')[1].split('\n')[1]
         filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt'%PanNO
         with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text).replace('\t','').replace('\n\n','\n'))


        else:
            pass


# folder_path = 'src/extracts'
# paths = os.listdir(folder_path)
# arr = []
# aadhar_arr = []
# for path in paths:
#     fpath = folder_path+'/'+path

#     if fpath not in arr:
#         arr.append(fpath)
#         with open(fpath, "r", encoding="utf-8") as file:
#             string = file.read()

#             aadhar_no_form = re.search(
#                 r'^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$', string)
#             full_name = string.split('Name')[1].split('\n')[1]
#             dob = string.split('DOB')[0].split('\n')[0]
#             gender = ''

#             if string.__contains__('Female'):
#                 gender = 'Female'
#             else:
#                 gender = 'Male'

#             aadharObj = {
#                 "Adhar_Card_No": aadhar_no_form,
#                 "Full_Name": full_name,
#                 "DOB": dob,
#                 "Gender": gender
#             }
#             aadhar_arr.append(aadharObj)
#     else:
#         pass


# print(aadhar_arr)