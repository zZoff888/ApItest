from Config.config import bady_Path
from Untils.public.ReadExcel import ReadExcel

s = ReadExcel.readExcel(bady_Path, "需求")
inter = s[0]["url"]
print(inter)