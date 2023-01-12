import os

class ExtractAndForward():
    def __init__(self):
        pass    


    def ImageSplitter(self):
        pass


    def ExtractAadhar(self):
        filesPaths = self.FindPaths()

        if len(filesPaths) > 0:
            docs = ['']


            """ Initiate image splitter here """


    def FindPaths(self):
        folder_path = 'src/test'
        paths = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                paths.append(file_path.replace("\\", "/"))

                return paths

                
            
    
files = ExtractAndForward()
files.ExtractAadhar()


