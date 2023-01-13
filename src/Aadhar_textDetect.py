import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ExtractData():
   def __init__(self,file):
      self.file=file
      print("Extract Data",file)
      image=cv2.imread('src/test/adharcard.jpg');
      text = pytesseract.image_to_string(image,lang='eng + hin')
      print(text)


      pass