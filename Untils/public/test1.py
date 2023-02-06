import os
import yaml
import copy
from Untils.public.read_yaml import read_Yaml
import time
import pandas as pd


class read_report():
    moudlename=None
    list3=[]
    dictNew = {}
    dictOld={}
    dictNewxx={}
    dictOldxx={}
    dictNew1={}
    @classmethod
    def gas_report(cls,NewFileName,OldFileName):
        Newdata=read_Yaml.readYaml(f"{NewFileName}")
        Olddata=read_Yaml.readYaml(f"{OldFileName}")

        for i in Newdata:
            cls.moudlename=i
            # print(a)
            Newlen=Newdata.get(cls.moudlename)
            Oldlen=Olddata.get(cls.moudlename)
            # print(len(v))
            if Oldlen!=None:\

                Newflilelistlen=len(Newlen)
                Oldflilelistlen=len(Oldlen)
            # print(v1,type(v))
                if Newflilelistlen <= Oldflilelistlen:
                    cls.dictNewxx = {}
                    for i in range(0, Newflilelistlen):
                        NewWay = Newlen[i]
                        OldWay = Oldlen[i]
                        differ = set(NewWay.keys()) & set(OldWay.keys())
                        if differ == set():
                            differ = ""
                        elif differ != set():
                            data = str(differ)
                            for i in data:
                                # # # print(data.replace("(", ""))
                                data = data.translate(str.maketrans({'{': '', '}': '', "'": ''}))
                                Newvalue = NewWay[f"{data}"]
                                Oldvalue = OldWay[f"{data}"]
                            cls.dictNewxx[f'{data}'] = Newvalue
                            cls.dictOldxx[f'{data}'] = Oldvalue
                            # print(cls.dictNewxx)
                            x = cls.dictNewxx[f"{data}"]
                            y = cls.dictOldxx[f"{data}"]
                            # print(x)
                            cls.dictNewxx[f'{data}'] = x - y
                            if cls.dictNewxx[f'{data}'] == 0:
                                del cls.dictNewxx[f'{data}']
                    cls.list3.append(cls.dictNewxx)
        # print(cls.list3)
        for i in cls.list3:
            # print(i)
            list4=[]
            list4.append(i)
            # print(list4)
                        cls.dictNew[f'{cls.moudlename}']=list4
                        print(cls.dictNew)
            # if i :
            #     cls.list3.append(i)
                # print(i,type(i))
                            # cls.list3.remove(i)
                # return
        # print(cls.list3)
                    # cls.dictNew[f'{cls.moudlename}'] = cls.dictNewxx
        # for i in cls.dictNew.copy():
        #     if not bool(cls.dictNew[i]):
        #         del cls.dictNew[i]
        # pd.read_json(cls.dictNew)
        # print(cls.dictNew)



read_report.gas_report("test",'gasdata20230131145638')



