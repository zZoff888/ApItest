import yaml
from Config.config import data_Path
import os

# f = open(yaml_Path, "r")
# # 轉換方法1
# # data=yaml.load(f, Loader=yaml.CLoader)
# # 方法2
# # data=yaml.load(f,Loader=yaml.FullLoader)
# # 方法3
# data=yaml.safe_load(f)
# f.close()
# print(data)

class read_Yaml():
    # 讀取文件
    # data={}
    def readYaml(filename):
        yaml_Path = os.path.join(data_Path, f'{filename}.yaml')
        f=f = open(yaml_Path, "r")
        data=yaml.safe_load(f)
        f.close()
        # print(data)
        return data
    # 覆盖写入
    def generate_yaml_doc(data,filename):
        yaml_Path = os.path.join(data_Path, f"{filename}.yaml")

        with open(yaml_Path, "w", encoding="utf-8") as f:
            yaml.dump(data, f)



read_Yaml.readYaml("test")
# py_object = {'school': 'zhang',
#              'students': ['a', 'b']}
# read_Yaml.generate_yaml_doc(py_object,"gg")

