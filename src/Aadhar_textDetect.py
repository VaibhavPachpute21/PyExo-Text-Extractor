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

        if ("आधार" in string) or ("अधिकार" in string):
            aadhar_no = re.search(r"\d{4}\s\d{4}\s\d{4}", string).group(0)
            filePath = os.getcwd()+'\\src\\extracts\\%s_aadhar.txt' % aadhar_no
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(string.replace('\t', '').replace('\n\n', '\n'))

        if ('Permanent Account Number' in string):
            # PanNO = str(string).split('Number')[1].split('\n')[1]
            PanNO=re.search(r"[A-Z]{5}[0-9]{4}[A-Z]",string).group(0)
            filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt'%PanNO
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(string).replace('\t', '').replace('\n\n', '\n'))

        if ("Balance" in string) or ("Credit" in string) or ("Debit" in string) or ("Account Statement" in string) or ("Account Summary" in string) or ("Transaction" in string) or ("Transactions" in string) or ("Withdrawal" in string):
            img_cv = cv2.imread(file)

            img_resized = cv2.resize(img_cv,
                                    (int(img_cv.shape[1] + (img_cv.shape[1] * .1)),
                                    int(img_cv.shape[0] + (img_cv.shape[0] * .25))),
                                    interpolation=cv2.INTER_AREA) 
            img_rgb = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
            output = pytesseract.image_to_string(img_rgb)

            file = file.split('/')[-1].split('.')[0]
            filePath = os.getcwd()+'\\src\\extracts\\%s_statement.txt' % file

            with open(filePath,'w', encoding="utf-8") as f: 
                f.write(output) 

            
            


folder_path = 'src/extracts'
paths = os.listdir(folder_path)
arr = []
aadhar_arr = []
pan_arr=[]
for path in paths:
    fpath = folder_path+'/'+path
    
    if fpath not in arr:
        arr.append(fpath)

        
        if "_aadhar.txt" in fpath:
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
                
        elif "_pan.txt" in fpath:
            with open(fpath, "r", encoding="utf-8") as file:
                string = file.read()

                full_name =''
                father_name=''
                PanNO=re.search(r"[A-Z]{5}[0-9]{4}[A-Z]",string).group(0)
                try:
                    dob = re.search(r'\d{2}/\d{2}/\d{4}', string).group(0)
                except:
                    pass
                if string.__contains__('पिता'):
                    full_name=string.split('पिता')[0].strip().split('\n')[-1]
                    father_name=string.split('पिता')[1].strip().split('\n')[1]
                    # print(father_name)

                elif string.__contains__('नाम / Name'):
                    full_name=string.split('नाम / Name')[-1].strip().split('\n')[0]
                    # print('fname',full_name)
                pan_obj={
                    "Pan No: ":PanNO,
                    "Name: ":full_name,
                    "Father's Name":father_name,
                    "DOB: ":dob
                }
                pan_arr.append(pan_obj);
                # print(pan_arr);
        
    else:
        pass

print("Aadhar Cards:")
print(aadhar_arr)
print("Pan Cards:")
print(pan_arr)