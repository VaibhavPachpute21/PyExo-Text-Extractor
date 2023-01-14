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
        print(file)
        text = pytesseract.image_to_string(image, lang='eng+hin+mar')
        string = str(text)
        # print(string)

        # match2 = re.search(r"\d{4}\s\d{4}\s\d{4}", string)
        # match3 = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]{1}', string)
        # for Aadhar Card
        if ("आधार" in string) or ("अधिकार" in string):
            aadhar_no = re.search(r"\d{4}\s\d{4}\s\d{4}", string).group(0)
            filePath = os.getcwd()+'\\src\\extracts\\%s_aadhar.txt' % aadhar_no
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(string.replace('\t', '').replace('\n\n', '\n'))

        if ('Permanent Account Number' in string):
            PanNO = str(string).split('Number')[1].split('\n')[1]
            filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt'%PanNO
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(string).replace('\t', '').replace('\n\n', '\n'))

        else:
            print(file)
            # print(string)


folder_path = 'src/extracts'
paths = os.listdir(folder_path)
arr = []
aadhar_arr = []
for path in paths:
    fpath = folder_path+'/'+path

    if fpath not in arr:
        arr.append(fpath)
        with open(fpath, "r", encoding="utf-8") as file:
            string = file.read()

            aadhar_no_form = re.search(r"\d{4}\s\d{4}\s\d{4}", string).group(0)

            full_name = string.split('जन्म')[0].split('\n')[-2]

            result = re.sub(r'[^a-zA-Z]', '', full_name)
            name_result = ''
            for i, c in enumerate(result):
                if c.isupper() and i != 0:
                    name_result += " "
                name_result += c

            try:
                dob = re.search(r'\d{2}/\d{2}/\d{4}', string).group(0)

            except:
                pass

            gender = ''

            if string.__contains__('Female' or 'FEMALE'):
                gender = 'Female'
            else:
                gender = 'Male'

            aadharObj = {
                "Adhar_Card_No": aadhar_no_form,
                "Full_Name": name_result,
                "DOB": dob,
                "Gender": gender
            }
            aadhar_arr.append(aadharObj)
    else:
        pass

# print(aadhar_arr)
