import os

class ExtractAndForward():
    def __init__(self, name):
        self.name = name

    def ExtractAadhar(self):
        folder_path = '/path/to/folder'

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                    print(content)
            
    



