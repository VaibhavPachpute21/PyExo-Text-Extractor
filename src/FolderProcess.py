import os
import cv2


class ExtractAndForward():
    def __init__(self):
        pass    


    def ImageSplitter(self,i,j):

        img = cv2.imread(i)
        template = cv2.imread(j)

        bnwImg1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        

        bnwImg2=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
        cv2.imshow('GRAY Template IMG',bnwImg2)
        cv2.waitKey(0)

        """ Match """

        img_copy = img.copy()


        result = cv2.matchTemplate(img_copy, template, cv2.TM_CCOEFF_NORMED)

     
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        
        w, h = template.shape[1], template.shape[0]

        
        cropped = img_copy[max_loc[1]:max_loc[1]+h, max_loc[0]:max_loc[0]+w]
        cv2.imshow('GRAY Template IMG',cropped)
        cv2.waitKey(0)
               

    def ExtractAadhar(self):
        filesPaths = self.FindPaths()
        print(filesPaths)
        if len(filesPaths) > 0:
            templates = ['src/imgs/templates/aadharFront.jpg','src/imgs/templates/driving.jpg','src/imgs/templates/pan.jpg','src/imgs/templates/passport.png','src/imgs/templates/voter-id.jpg']
            for i in filesPaths:
                for j in templates:
                    self.ImageSplitter(i,j)
                
            


    def FindPaths(self):
        folder_path = 'src/test'
        arr=[]
        paths=os.listdir(folder_path)
        for path in paths:
            fpath=folder_path+'/'+path
            print(fpath)
            arr.append(fpath)
        
        return arr

                
            
    
files = ExtractAndForward()
files.ExtractAadhar()

