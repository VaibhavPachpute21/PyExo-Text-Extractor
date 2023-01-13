import os
import cv2
from Aadhar_textDetect import ExtractData


class ExtractAndForward():
    def __init__(self):
        self.iterator = 0
        self.InterMediateMax = []
        self.MaxMatches = []
        self.InterMediateFilePaths = []
        self.MatchedPaths = []


    def ProvideOutput(self,file):

        fileName = file.split('/')[-1]
        
        opimg = cv2.imread(file)
        fulPath=os.getcwd()+'\\src\\outputs\\%s'%fileName

        # cv2.imwrite(fulPath ,opimg)
        # cv2.imshow('Output Images', opimg)
        # cv2.waitKey(0)
        ExtractData(file)



    def ImageSplitter(self,filePath,templatePath):
        img = cv2.imread(filePath)
        template = cv2.imread(templatePath)
        img = cv2.resize(img, template.shape[:2][::-1], interpolation = cv2.INTER_LINEAR)
        

        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img, None)
        kp2, des2 = sift.detectAndCompute(template, None)


        matcher = cv2.FlannBasedMatcher()
        matches = matcher.knnMatch(des1, des2, k=2)


        good_matches = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good_matches.append(m)
        
        percent_match = (len(good_matches) / len(kp1)) * 100
        self.InterMediateMax.append(percent_match)
        self.InterMediateFilePaths.append(filePath)
  
        if len(self.InterMediateMax) == 5:
            self.MaxMatches.append(max(self.InterMediateMax))
            max_ind = self.InterMediateMax.index(max(self.InterMediateMax))
            self.MatchedPaths.append(self.InterMediateFilePaths[max_ind])

            self.InterMediateMax = []
            self.InterMediateFilePaths = []
        
        img3 = cv2.drawMatches(img, kp1, template, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
  

        if len(self.MatchedPaths) == 4:

            for x in range(0, len(self.MatchedPaths)):
                self.ProvideOutput(self.MatchedPaths[x])
        
        
        """ cv2.imshow('Matched Images', img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows() """



               

    def ExtractAadhar(self):
        filesPaths = self.FindPaths()

        if len(filesPaths) > 0:
            templates = ['src/imgs/templates/aadharFront.jpg','src/imgs/templates/driving.jpg','src/imgs/templates/pan-card.png','src/imgs/templates/passport.png','src/imgs/templates/voter1.jpg']
            for filePath in filesPaths:
                for templatePath in templates:
                    self.ImageSplitter(filePath,templatePath)


    def FindPaths(self):
        folder_path = 'src/test'
        arr=[]
        paths=os.listdir(folder_path)
        for path in paths:
            fpath=folder_path+'/'+path
            
            arr.append(fpath)
                
        return arr


files = ExtractAndForward()
files.ExtractAadhar()

