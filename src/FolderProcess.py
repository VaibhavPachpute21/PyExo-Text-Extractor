import os
import cv2


class ExtractAndForward():
    def __init__(self):
        pass    


    def ImageSplitter(self,filePath,templatePath):
        img = cv2.imread(filePath)
        template = cv2.imread(templatePath)
        
    
        orb = cv2.ORB_create(nfeatures=500)
        kp1, des1 = orb.detectAndCompute(img, None)
        kp2, des2 = orb.detectAndCompute(template, None)
        
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        
        matches = sorted(matches, key=lambda x: x.distance)
        
        match_img = cv2.drawMatches(img, kp1, template, kp2, matches[:50], None)
    
        # Find the number of matches
        num_matches = len(matches)

        # Find the percentage match
        percent_match = (num_matches / len(kp1)) * 100
        print("Percentage match: ", percent_match)

        cv2.imshow('Matc',match_img)
        cv2.waitKey(0)


               

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

