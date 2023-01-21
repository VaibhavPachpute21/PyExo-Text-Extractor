from PyExo import PyExo
import os
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Files = PyExo.Extract_From_Pdf(pdfFile=r'D:\Web\\eCell\src\\test-pdf\\test.pdf')
data = PyExo.ExtractDocumentsData(filePaths=Files)

