import os;
import re;
import copy;
from datetime import time
import time
import yaml;
from Untils.public.read_yaml import read_Yaml
class GasTurnYaml():
    def __init__(self,fileRoot):
        self.fileroot=fileRoot
        # self.saveroot=saveRoot

    # 读取txt文件
    def  readGasFile(self):
        lineData=[]
        for line in open(self.fileroot).readlines():
            lineData.append(line)
        return lineData;

    # 分割字符串
    def splitData(self):
        line=self.readGasFile()
        lineD=[]
        for i in line:
            # print(i)
            if i == "\n":
                lineD.append(i)
            elif re.search(r'(Test result: *)', i) :
                continue
            elif re.search(r'(Running [\d*?] test\w\s|\sfor *)', i) :
                # print(re.split("for ",re.split(r'(Running [\d*?] test\w\s|\sfor )', i)[-1])[-1])
                lineD.append(re.split("for ",re.split(r'(Running [\d*?] test\w\s|\sfor )', i)[-1])[-1])
            elif  re.search(r'(.*\]\[.m )', i) :
                lineD.append(re.split(r'(.*\]\[.m )',i)[-1])
            else:
                continue
        return lineD;

    # 转为字典
    def lineToDir(self):
        lineD = self.splitData()
        dir={}
        title=None
        content=[]
        for i in lineD:
            if "\n" == i:
                dir[copy.copy(title)] = content.copy()
                title=None
                content.clear()
                continue
            if re.search(r"(.*\.t\.sol*)" ,i) :
                title=re.split('\n',i)[0]
            if re.search(r'(.* \Sgas*)',i):
                spl=re.split(r'( \Sgas: )', i)
                content.append({spl[0] : int(re.split(r'\S\n', spl[-1])[0])})
        del dir[None]
        return dir;

    # 保存为yaml
    def dirToYaml(self):
        dir=self.lineToDir()
        s = time.strftime("%Y%m%d%H%M%S", time.localtime()) #生成当前时间
        Newname = "gasdata" + s
        read_Yaml.generate_yaml_doc(dir, Newname)
        # with open(self.saveroot, 'w') as file:
        #     file.write(yaml.dump(dir, allow_unicode=True))
a='/Users/mac/Desktop/detask/code-market/report1.txt'
GasTurnYaml(a).dirToYaml()