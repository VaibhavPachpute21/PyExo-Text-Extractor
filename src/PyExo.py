import os
from DocumentTextDetection import ExtractData
import fitz
import docx2txt
from DocumentObject import CaptureData

class PyExo():
    def __init__(self):
        pass

    def Extract_From_Doc(self, filepath):
        text = docx2txt.process(filepath, r"src\\wordtoimg")

        folder_path = 'src/wordtoimg'
        arr = []
        paths = os.listdir(folder_path)
        for path in paths:
            fpath = folder_path+'/'+path
            arr.append(fpath)
        if len(arr) == len(paths):
            return arr

    def Extract_From_Pdf(pdfFile):
        doc = fitz.open(pdfFile)
        for page_number in range(doc.page_count):
            page = doc[page_number]
            pix = page.get_pixmap()
            if (os.path.exists(os.path.join(os.getcwd()+'\\src', 'pdftoimg'))):
               pass
            else:
                os.mkdir(os.path.join(os.getcwd()+'\\src', 'pdftoimg'))
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

    def ExtractAadhar(filePaths):
        if len(filePaths) > 0:
            for x in filePaths:
                ExtractData(x)

                try:
                    CaptureData()
                except:
                    print("Error")

    def FindPaths(self):

        choice = int(
            input("Enter 0 for pdf or 1 for word file or 2 for images "))

        if choice == 0:
            RecieveImages = self.Extract_From_Pdf(
                os.getcwd()+'\\src\\test-pdf\\test.pdf')
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
            Images = self.Extract_From_Doc(
                os.getcwd()+'\\src\\test-word\\The Heading.docx')
            return Images


# files = PyExo()
# files.ExtractAadhar()
