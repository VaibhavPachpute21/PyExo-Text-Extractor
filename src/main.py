from PyExo import PyExo
import os
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Extract from pdf
""" Files = PyExo.Extract_From_Pdf(pdfFile=r'C:\\Users\\Dell\\OneDrive\\Documents\\Python\\E-cell\\Text-Extractor\\src\\test-pdf\\test.pdf')
data = PyExo.ExtractDocumentsData(filePaths=Files)
 """

# Extract from Word
WordImgs = PyExo.Extract_From_Doc(wordFile=r'C:\\Users\\Dell\\OneDrive\\Documents\\Python\\E-cell\\Text-Extractor\\src\\test-pdf\\test.pdf')
data = PyExo.ExtractDocumentsData(filePaths=WordImgs)
