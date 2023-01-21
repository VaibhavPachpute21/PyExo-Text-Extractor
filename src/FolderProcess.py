import os
from DocumentTextDetection import ExtractData
import fitz
from PIL import Image
import docx2txt


class ExtractAndForward():
    def __init__(self):
        pass

    
    def ConvertWordToImages(self,filepath):
        text = docx2txt.process(filepath,r"src\\wordtoimg")

        folder_path = 'src/wordtoimg'
        arr = []
        paths = os.listdir(folder_path)
        for path in paths:
            fpath = folder_path+'/'+path
            arr.append(fpath)

        if len(arr) == len(paths):
            return arr



    def ConvertPdfToImages(self,pdfFile):
        doc = fitz.open(pdfFile)

        
        for page_number in range(doc.page_count):
            
            page = doc[page_number]
            
            pix = page.get_pixmap()
            
            filePath = os.getcwd()+f'\\src\\pdftoimg\\{page_number}.png'
            pix.save(filePath)

            folder_path = 'src/pdftoimg'
            arr = []
            paths = os.listdir(folder_path)
            for path in paths:
                fpath = folder_path+'/'+path
                arr.append(fpath)

            if len(arr) == doc.page_count:
                return arr


    def ExtractAadhar(self):
        filesPaths = self.FindPaths()
        for x in filesPaths:
            ExtractData(x)

    def FindPaths(self):

        choice = int(input("Enter 0 for pdf or 1 for word file or 2 for images "))

        if choice == 0:
            RecieveImages = self.ConvertPdfToImages(os.getcwd()+'\\src\\test-pdf\\test.pdf')
            return RecieveImages
        elif choice == 1:
            folder_path = 'src/test'
            arr = []
            paths = os.listdir(folder_path)
            for path in paths:
                fpath = folder_path+'/'+path
                arr.append(fpath)
            return arr
        else:
            Images = self.ConvertWordToImages(os.getcwd()+'\\src\\test-word\\The Heading.docx')
            return Images


files = ExtractAndForward()
files.ExtractAadhar()
