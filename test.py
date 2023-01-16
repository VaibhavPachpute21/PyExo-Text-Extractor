import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import pytesseract
import table_ocr as tb
file = os.getcwd()+"\\src\\test\\bank2.jpg"



img_cv = cv2.imread(file)
img_resized = cv2.resize(img_cv,
                         (int(img_cv.shape[1] + (img_cv.shape[1] * .1)),
                          int(img_cv.shape[0] + (img_cv.shape[0] * .25))),
                         interpolation=cv2.INTER_AREA) 
img_rgb = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
output = pytesseract.image_to_string(img_rgb)
with open('test.csv','w') as f: 
    f.write(output) 

""" def invert_area(image, x, y, w, h, display=False):
    ones = np.copy(image)
    ones = 1
    
    image[ y:y+h , x:x+w ] = ones*255 - image[ y:y+h , x:x+w ] 
    
    if (display): 
        cv2.imshow("inverted", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image
left_line_index = 17
right_line_index = 20
top_line_index = 0
bottom_line_index = -1
    
cropped_image, (x, y, w, h) = get_ROI(img, horizontal, vertical, left_line_index, right_line_index, top_line_index, bottom_line_index)
gray = get_grayscale(img)
bw = get_binary(gray)
bw = invert_area(bw, x, y, w, h, display=True)
 """
""" 
voterList = ['voter.jpg','voter1.jpg','voter2.jpg','voter3.jpg','voter4.jpg']
allFiles = os.listdir(path)

voterArr=[]
for file in voterList:
    imPath = path+'\\'+file
    # print(imPath)
    filePath = os.getcwd()+'\\src\\extracts\\%s_voter.txt'%file
    image = cv2.imread(imPath)
    kernel=np.array([[-1,-1,-1], [-1,5,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    cv2.imshow("sharp",sharpened)
    cv2.waitKey(0)
    text = pytesseract.image_to_string(sharpened, lang='eng+hin+mar')

    with open(filePath, "w", encoding="utf-8") as file:
                file.write(str(text).replace('\t', '').replace('\n\n', '\n'))
    
    print(text)
    if str(text).__contains__('ELECTION'):
        electors_Name=''
        father_name=''
        husband_name=''
        gender=''

    #     newArr=str(text).split('\n')
    #     for i in newArr:
    #         if ("Elector") in i :
    #             electors_Name= i.split('Name')[1].replace(":","").strip()
    #         if ("Eléctor") in i:
    #             electors_Name= i.split('Name')[1].replace(":","").strip()
    #         if ("Father") in i:
    #             father_name= i.split('Name')[1].replace(":","").strip()
    #         if ("Husband") in i:
    #             husband_name=i.split('Name')[1].replace(":","").strip()
    #         if "Male" in i:
    #             gender="Male"
    #         if "Female" in i:
    #             gender="Female"

    #     voterObj={
    #         "Name:": electors_Name,
    #         "Father Name:":father_name,
    #         "Husband Name:":husband_name,
    #         "Gender:":gender
    #     }
    #     voterArr.append(voterObj)
            
        with open(filePath, "w", encoding="utf-8") as file:
            file.write(str(text).replace('\t', '').replace('\n\n', '\n'))
    else:
        # print(str(text))
        # print("didn't found: ", imPath)
        pass
print(voterArr) """
