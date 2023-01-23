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

        # Checking for Aadhaar Card data
        if ("आधार" in string) or ("अधिकार" in string):
            fileSplitted = file.split('/')[-1]
            print("Checking for Aadhaar data in",fileSplitted,'\n')  
                
            aadhar_no = re.search(r"\d{4}\s\d{4}\s\d{4}", string).group(0)
            filePath = os.getcwd()+'\\src\\extracts\\%s_aadhar.txt' % aadhar_no
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(string.replace('\t', '').replace('\n\n', '\n'))
        
        #Checking for PAN card Data
        if ('Permanent Account Number' in string):
            print("Checking for Pan data in",file.split('/')[-1],'\n')
            # PanNO = str(string).split('Number')[1].split('\n')[1]
            PanNO = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", string).group(0)
            filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt' % PanNO
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(string).replace('\t', '').replace('\n\n', '\n'))

        #Checking for voter card Data
        if ('ELECTION' in string) or ('Election' in string):
            print("Checking for Voter data in",file.split('/')[-1],'\n')
            file = file.split('/')[-1].split('.')[0]
            filePath = os.getcwd()+'\\src\\extracts\\%s_voter.txt' % file
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(string).replace('\t', '').replace('\n\n', '\n'))

        #Checking for Bank statement Data
        if ("Balance" in string) or ("Credit" in string) or ("Debit" in string) or ("Account Statement" in string) or ("Account Summary" in string) or ("Transaction" in string) or ("Transactions" in string) or ("Withdrawal" in string):
            print("Checking for Bank Statement data in",file.split('/')[-1],'\n')
            img_cv = cv2.imread(file)
            img_resized = cv2.resize(img_cv,
                                     (int(img_cv.shape[1] + (img_cv.shape[1] * .1)),
                                      int(img_cv.shape[0] + (img_cv.shape[0] * .25))),
                                     interpolation=cv2.INTER_AREA)
            img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
            output = pytesseract.image_to_string(img_rgb)
            newArr=str(output).split('\n')
            for row in newArr:
                    if ("Date" in row):
                        spliter=row
                        if ("Balance" in spliter):
                            formData=str(output).split(spliter)[0]+spliter.replace(' ',',')+ str(output).split(spliter)[1].replace(' ',',')
                            file = file.split('/')[-1].split('.')[0]
                            filePath = os.getcwd()+'\\src\\extracts\\%s_statement.csv' % file
                            with open(filePath, 'w', encoding="utf-8") as f:
                                f.write(formData)

        #Checking for Salary slip Data
        if ("Basic Salary" in string) or ("Provident Fund" in string) or ("Allowance" in string):
            print("Checking for Salary slip data in",file.split('/')[-1],'\n')
            file = file.split('/')[-1].split('.')[0]
            filePath = os.getcwd()+'\\src\\extracts\\%s_salarySlip.txt' % file
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(string).replace('\t', '').replace('\n\n', '\n'))
        
        #Checking for Passport Data
        if ('REPUBLIC OF INDIA' in string) or ('Passport' in string):
            print("Checking for Passport data in",file.split('/')[-1],'\n')
            file = file.split('/')[-1].split('.')[0]
            filePath = os.getcwd()+'\\src\\extracts\\%s_passport.txt' % file
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(string).replace('\t', '').replace('\n\n', '\n'))
        

        

