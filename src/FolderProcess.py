import os
import cv2


class ExtractAndForward():
    def __init__(self):
        self.iterator = 0
        self.InterMediateMax = []
        self.MaxMatches = []
        self.InterMediateFilePaths = []
        self.MatchedPaths = []

    def ImageSplitter(self,filePath,templatePath):
        img = cv2.imread(filePath)
        template = cv2.imread(templatePath)
        img = cv2.resize(img, template.shape[:2][::-1], interpolation = cv2.INTER_LINEAR)
        # template = cv2.resize(template, img.shape[:2][::-1], interpolation = cv2.INTER_LINEAR)
        # img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # template=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
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
        # print(percent_match)

        self.InterMediateMax.append(percent_match)
        self.InterMediateFilePaths.append(templatePath)

        self.iterator = self.iterator + 1
       
        if self.iterator == 5:
            self.MaxMatches.append(max(self.InterMediateMax))
            max_ind = self.MaxMatches.index(max(self.MaxMatches))
            self.MatchedPaths.append(self.InterMediateFilePaths[max_ind])
            self.iterator = 0   
            self.InterMediateMax = []
        print(self.iterator)

        



        img3 = cv2.drawMatches(img, kp1, template, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        


        self.iterator = self.iterator + 1
       
        # if self.iterator == 5:

        #     self.MaxMatches.append(max(self.InterMediateMax))
        #     max_ind = self.MaxMatches.index(max(self.MaxMatches))

        #     self.MatchedPaths.append(self.InterMediateFilePaths[max_ind])
        #     self.iterator = 0   
        #     self.InterMediateMax = []
        
        cv2.imshow('Matched Images', img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # print(self.MatchedPaths)
        # print(percent_match)
        # cv2.imshow('Matc',match_img)
        # cv2.waitKey(0)



               

    def ExtractAadhar(self):
        filesPaths = self.FindPaths()
        print(filesPaths)
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
            print(fpath)
            arr.append(fpath)
        
        return arr


files = ExtractAndForward()
files.ExtractAadhar()

