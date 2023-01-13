import pytesseract
import cv2
import os
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'
class ExtractData():
   def __init__(self,file):
      self.file=file

      image=cv2.imread(file);

      text = pytesseract.image_to_string(image,lang='eng+hin')

      string = text

      # Check if the string contains 12 digits using regular expression
      match = re.search(r'\d{12}', string)

      if match:
         print(text)
      else:
         print("The string does not contain 12 digits.")


      pass