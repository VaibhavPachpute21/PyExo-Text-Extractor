import os
from Aadhar_textDetect import ExtractData



class ExtractAndForward():
    def __init__(self):
        pass

    def ExtractAadhar(self):
        filesPaths = self.FindPaths()
        for x in filesPaths:
            print(x)
            ExtractData(x)

    def FindPaths(self):
        folder_path = 'src/test'
        arr = []
        paths = os.listdir(folder_path)
        for path in paths:
            fpath = folder_path+'/'+path
            arr.append(fpath)
        return arr


files = ExtractAndForward()
files.ExtractAadhar()
