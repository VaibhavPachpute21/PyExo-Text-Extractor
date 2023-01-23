import os
import re
import json

def CaptureData():
        
        folder_path = 'src/extracts'
        paths = os.listdir(folder_path)
        arr = []
        aadhar_arr = []
        pan_arr = []
        voterArr=[]
        salarySlipArr=[]
        passport_arr=[]

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

                        gender = 'NA'
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
                        full_name = 'NA'
                        father_name = 'NA'
                        PanNO = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", string).group(0)
                        try:
                            dob = re.search(r'\d{2}/\d{2}/\d{4}', string).group(0)
                        except:
                            pass
                        if string.__contains__('पिता'):
                            full_name = string.split('पिता')[0].strip().split('\n')[-1]
                            father_name = string.split(
                                'पिता')[1].strip().split('\n')[1]
                            

                        elif string.__contains__('नाम / Name'):
                            full_name = string.split(
                                'नाम / Name')[-1].strip().split('\n')[0]
                            
                        pan_obj = {
                            "Pan No": PanNO,
                            "Name": full_name,
                            "Father's Name": father_name,
                            "DOB": dob
                        }
                        pan_arr.append(pan_obj)
                
                elif "_voter.txt" in fpath:
                    with open(fpath, "r", encoding="utf-8") as file:
                        string = file.read()
                        electors_Name = ''
                        father_name = 'NA'
                        husband_name = 'NA'
                        gender = 'NA'
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
                            "Name": electors_Name,
                            "Father Name": father_name,
                            "Husband Name": husband_name,
                            "Gender": gender
                        }
                        voterArr.append(voterObj)

                elif "_statement.csv" in fpath:
                    with open(fpath, "r", encoding="utf-8") as file:
                        string = file.read()
                        fileName=fpath.split('/')[-1].split('.')[0]
                        newArr=string.split('\n')
                        for row in newArr:
                            if ("Date" in row):
                                spliter=row
                                if ("Balance" in spliter):
                                    pass
                                    
                
                elif "_salarySlip.txt" in fpath:
                    with open(fpath, "r", encoding="utf-8") as file:
                        empcode='NA'
                        empname='NA'
                        PanNO='NA'
                        pf='NA'
                        uan='NA'
                        earn='NA'
                        string = file.read()
                        salSlipLine=string.split('\n')
                        for line in salSlipLine:
                            if ("Employee Code" in line):
                                lw=line.split()
                                empcode=lw[lw.index("Code")+1]
                                # print(empcode)
                            if ("Employee Name" in line):
                                lw=line.split()
                                empname=lw[lw.index("Name")+1] +' '+lw[lw.index("Name")+2]
                            if ("PAN" in line):
                                try:
                                    PanNO = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", line).group(0)
                                except:
                                    pass
                                
                            if ("Basic Salary" in line):
                                lw=line.split()
                                basicSal=lw[lw.index("Salary")+1]
                                
                            if ("Provident Fund" in line):
                                lw=line.split()
                                pf=lw[lw.index("Fund")+1]
                            if ('UAN Number' in line):
                                lw=line.split()
                                uan=lw[lw.index("Number")+1]
                            if ("Total Earnings" in line):
                                lw=line.split()
                                earn=lw[lw.index("Earnings")+1]


                        salSlipObject={
                                "Employee Name": empname,
                                "Employee Code":empcode,
                                "Pan No":PanNO,
                                "Provident Fund":pf,
                                "UAN Number" : uan,
                                "Total Earnings":earn
                            }
                        salarySlipArr.append(salSlipObject)
            
                elif "_passport.txt" in fpath:
                    with open(fpath, "r", encoding="utf-8") as file:
                        string = file.read().strip()
                        stringArr=string.split('\n')
                        dt=re.findall(r'\d{2}/\d{2}/\d{4}', string)
                        lastLine=stringArr[-1]
                        slastLine=stringArr[-2]

                        passportObj={
                            "PassportNo":lastLine.split('<')[0],
                            "Type":slastLine.split('<')[0],
                            "Nationality":slastLine.split('<')[1][0:3],
                            "First Name":slastLine.split('<')[3],
                            "Last Name":slastLine.split('<')[1].replace(slastLine.split('<')[1][0:3],''),
                            "DOB":dt[0],
                            "Date of issue:":dt[1],
                            "Date of Expiry:":dt[2]
                        }
                        passport_arr.append(passportObj)
            else:
                pass


        retArray={
            "Adhar Cards":aadhar_arr,
            "Pan Cards":pan_arr,
            "Voter Cards":voterArr,
            "Salary Slips":salarySlipArr,
            "Passports":passport_arr
        }
        json_string = json.dumps(retArray,indent=4)
        with open('documentsData.json', 'w') as outfile:
            outfile.write(json_string)
        return retArray

