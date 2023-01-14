import pytesseract
import cv2
import os
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

class ExtractData():
   def __init__(self,file):
      self.file=file

      image=cv2.imread(file)

      text = pytesseract.image_to_string(image,lang='eng+hin+mar')
      string = str(text)
      print(string)      

      match2 = re.search(r"\d{4}\s\d{4}\s\d{4}", string)



      if ("आधार" in string) or ("अधिकार" in string) or ("पहचान" in string):
         filePath = os.getcwd()+'\\src\\extracts\\%s'%match2.group(0)+'_aadhar'

         with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(string))
            
      
          
            
         

      else:
         pass

   

    
         
         


         



""" folder_path = 'src/extracts'
paths=os.listdir(folder_path)
arr = []
aadhar_arr = []
for path in paths:
   fpath=folder_path+'/'+path

   if fpath not in arr:
      arr.append(fpath)
      with open(fpath, "r", encoding="utf-8") as file:
            string = file.read()
            
            aadhar_no_form = re.search(r'\d{10}',string).group(0)
            full_name = string.split('Name')[1].split('\n')[1]
            dob = string.split('DOB')[1].split('\n')[0].split(' ')[1]
            gender = ''

            if string.__contains__('Female'):
               gender = 'Female' 
            else:
               gender = 'Male' 
            
            aadharObj = {
               'aadhar_no_form':aadhar_no_form,
               'full_name': full_name,
               'dob':dob,
               'gender':gender
            }
            
            aadhar_arr.append(aadharObj)


   else:
      pass



print(aadhar_arr) """