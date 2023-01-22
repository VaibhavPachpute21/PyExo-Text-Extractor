import os
from DocumentTextDetection import ExtractData
import fitz
import docx2txt
from DocumentObject import CaptureData
import cv2
from keras.models import load_model
import numpy as np

class PyExo():
    def __init__(self):
        pass

    def Extract_From_Doc(wordFile):

        if str(wordFile).endswith(".docx"):
            text = docx2txt.process(wordFile, r"src\\wordtoimg")
            
            folder_path = 'src/wordtoimg'
            arr = []
            paths = os.listdir(folder_path)
            for path in paths:
                fpath = folder_path+'/'+path
                arr.append(fpath)
            if len(arr) == len(paths):
                return arr
        else:
            print("Provide Word document")
            return []

    def Extract_From_Pdf(pdfFile):
        print(pdfFile)
        if str(pdfFile).endswith(".pdf"):
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
        else:
            print("Provide pdf document")
            return []

    def ExtractDocumentsData(filePaths):
        documentsList=['aadhaar','pan','voter','salary','bank','passport']
        if len(filePaths) > 0:
            for x in range(0,len(filePaths)):
                img=cv2.imread(filePaths[x])
                # cv2.imshow("img",img)
                model = load_model('./src/model/keras_model.h5', compile=False)
                labels = open('./src/model/labels.txt', 'r').readlines()
                image = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
                image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
                image = (image / 127.5) - 1
                probabilities = model(image)
                probaboility=labels[np.argmax(probabilities)].split(' ')[1]

                if (probaboility.strip() in documentsList):
                    print("\nDocument identified as",probaboility.strip())
                    ExtractData(filePaths[x])
                else:
                    print("Document Not Matched")

                if x == len(filePaths)-1:
                    try:
                        capturedData=CaptureData()
                        return capturedData;
                    except:
                        print("Error")

    def Extract_From_Images(folderPath):

        if str(folderPath).endswith('.pdf') or str(folderPath).endswith('.docx'):
            pass
        else:
            folder_path = folderPath
            arr = []
            paths = os.listdir(folder_path)
            for path in paths:
                fpath = folder_path+'/'+path
                if(str(fpath).endswith('.png') or str(fpath).endswith('.PNG') or str(fpath).endswith('.jpg') or str(fpath).endswith('.JPG') or str(fpath).endswith('.JPEG') or str(fpath).endswith('.jpeg') ):
                    arr.append(fpath)
            res=PyExo.ExtractDocumentsData(filePaths=arr)
            return res;
      


# files = PyExo()
# files.ExtractDocumentsData()
