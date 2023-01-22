from PyExo import PyExo
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

# Extract from pdf
# data = PyExo.Extract_From_Pdf(pdfFile=r'D:\Web\\eCell\src\\test\\test.pdf')

# Extract from Word
# data = PyExo.Extract_From_Doc(wordFile=r'D:\Web\\eCell\src\\test\\test.docx')

# Extract from Images
data = PyExo.Extract_From_Images(folderPath=r'D:\Web\\eCell\src\\test') 


print("Output",data)