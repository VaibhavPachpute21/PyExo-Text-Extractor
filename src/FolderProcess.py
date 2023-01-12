import os
import cv2


class ExtractAndForward():
    def __init__(self):
        pass    


    def ImageSplitter(self,i,j):
        print(i,j)


    def ExtractAadhar(self):
        filesPaths = self.FindPaths()
        print(filesPaths)
        if len(filesPaths) > 0:
            templates = ['src/imgs/templates/aadharFront.jpg','src/imgs/templates/driving.jpg','src/imgs/templates/pan.jpg','src/imgs/templates/passport.jpg']
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

