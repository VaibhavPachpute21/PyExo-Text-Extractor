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
      

      match1 = re.search(r'\d{10}', string)
      match2 = re.search(r"\d{4}\s\d{4}\s\d{4}", string)



      if match1 and ("आधार - आदमी का अधकिर" in string):
         filePath = os.getcwd()+'\\src\\extracts\\%s'%match1.group(0)+'_aadhar'

         with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(string))

      elif match2 and ("आधार - सामान्य माणसाचा अधिकार" in string):
         filePath = os.getcwd()+'\\src\\extracts\\%s'%match2.group(0)+'_aadhar'

         with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(string))


      else:
         pass
         





