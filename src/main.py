from PyExo import PyExo

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Extract from pdf
""" Files = PyExo.Extract_From_Pdf(pdfFile=r'C:\\Users\\Dell\\OneDrive\\Documents\\Python\\E-cell\\Text-Extractor\\src\\test-pdf\\test.pdf')
data = PyExo.ExtractDocumentsData(filePaths=Files)cls
 """

# Extract from Word
""" WordImgs = PyExo.Extract_From_Doc(wordFile=r'C:\\Users\\Dell\\OneDrive\\Documents\\Python\\E-cell\\Text-Extractor\\src\\test-word\\The Heading.docx')
data = PyExo.ExtractDocumentsData(filePaths=WordImgs)  """



# Extract from Images
ImageLinks = PyExo.Extract_From_Images(folderPath=r'C:\\Users\\Dell\\OneDrive\\Documents\\Python\\E-cell\\Text-Extractor\\src\\test') 
data = PyExo.ExtractDocumentsData(filePaths=ImageLinks)