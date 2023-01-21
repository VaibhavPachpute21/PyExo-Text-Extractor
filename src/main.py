from PyExo import PyExo
import os
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Files = PyExo.Extract_From_Pdf(pdfFile=r'C:\\Users\\Dell\\OneDrive\\Documents\\Python\\E-cell\\Text-Extractor\\src\\test-pdf\\test.pdf')
data = PyExo.ExtractAadhar(filePaths=Files)

