import cv2
from PIL import Image
from pdf2image import convert_from_path

documentsIMG=convert_from_path('D:\Web\eCell\src\\test\documents.pdf')

for document in range(len(documentsIMG)):
    documentsIMG[document].save('doc'+document+'.jpg','JPEG')
    # cv2.imshow('Document',documentsIMG[document])
    # cv2.waitKey(0)
print(self.MaxMatches.index(max(self.InterMediateMax)))
# bnwImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
# cv2.imshow('GRAY IMG',bnwImg);
# cv2.waitKey(0)