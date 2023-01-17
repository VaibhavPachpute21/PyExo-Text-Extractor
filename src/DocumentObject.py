import os
import re


folder_path = 'src/extracts'
paths = os.listdir(folder_path)
arr = []
aadhar_arr = []
pan_arr = []
voterArr=[]

for path in paths:
    fpath = folder_path+'/'+path
    if fpath not in arr:
        arr.append(fpath)
        if "_aadhar.txt" in fpath:
            with open(fpath, "r", encoding="utf-8") as file:
                string = file.read()
                aadhar_no_form = re.search(
                    r"\d{4}\s\d{4}\s\d{4}", string).group(0)
                full_name = string.split('जन्म')[0].split('\n')[-2]
                result = re.sub(r'[^a-zA-Z]', '', full_name)
                name_result = ''
                for i, c in enumerate(result):
                    if c.isupper() and i != 0:
                        name_result += " "
                    name_result += c
                try:
                    dob = re.search(r'\d{2}/\d{2}/\d{4}', string).group(0)
                except:
                    pass

                gender = ''
                if string.__contains__('Female' or 'FEMALE'):
                    gender = 'Female'
                else:
                    gender = 'Male'

                aadharObj = {
                    "Adhar_Card_No": aadhar_no_form,
                    "Full_Name": name_result,
                    "DOB": dob,
                    "Gender": gender
                }
                aadhar_arr.append(aadharObj)

        elif "_pan.txt" in fpath:
            with open(fpath, "r", encoding="utf-8") as file:
                string = file.read()
                full_name = ''
                father_name = ''
                PanNO = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", string).group(0)
                try:
                    dob = re.search(r'\d{2}/\d{2}/\d{4}', string).group(0)
                except:
                    pass
                if string.__contains__('पिता'):
                    full_name = string.split('पिता')[0].strip().split('\n')[-1]
                    father_name = string.split(
                        'पिता')[1].strip().split('\n')[1]
                    # print(father_name)

                elif string.__contains__('नाम / Name'):
                    full_name = string.split(
                        'नाम / Name')[-1].strip().split('\n')[0]
                    # print('fname',full_name)
                pan_obj = {
                    "Pan No: ": PanNO,
                    "Name: ": full_name,
                    "Father's Name": father_name,
                    "DOB: ": dob
                }
                pan_arr.append(pan_obj)
        
        elif "_voter.txt" in fpath:
            with open(fpath, "r", encoding="utf-8") as file:
                string = file.read()
                electors_Name = ''
                father_name = ''
                husband_name = ''
                gender = ''
                newArr = string.split('\n')
                for i in newArr:
                    if ("Elector") in i:
                        electors_Name = i.split('Name')[1].replace(":", "").strip()
                    if ("Eléctor") in i:
                        electors_Name = i.split('Name')[1].replace(":", "").strip()
                    if ("Father") in i:
                        father_name = i.split('Name')[1].replace(":", "").strip()
                    if ("Husband") in i:
                        husband_name = i.split('Name')[1].replace(":", "").strip()
                    if "Male" in i:
                        gender = "Male"
                    if "MALE" in i :
                        gender="Male"
                    if "Female" in i:
                        gender = "Female"
                    if "FEMALE" in i:
                        gender="Female"

                voterObj = {
                    "Name:": electors_Name,
                    "Father Name:": father_name,
                    "Husband Name:": husband_name,
                    "Gender:": gender
                }
                voterArr.append(voterObj)

        if "_statement.csv" in fpath:
            with open(fpath, "r", encoding="utf-8") as file:
                string = file.read()
                fileName=fpath.split('/')[-1].split('.')[0]
                newArr=string.split('\n')
                for row in newArr:
                    if ("Date" in row):
                        spliter=row
                        if ("Balance" in spliter):
                            pass
                            # print(string.split(spliter)[1])
               
    else:
        pass

print("Aadhar Cards:")
print(aadhar_arr)
print("Pan Cards:")
print(pan_arr)
print("Voter cards")
print(voterArr)
