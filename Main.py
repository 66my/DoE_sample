from Read_Write_CSV import *#line:1
from Generate_DOE import *#line:2
from User_input import *#line:3
import time #line:5
def execute_main ():#line:11
    ""#line:15
    O000000OO000OO000 ,OO000OO000OO000O0 =user_input ()#line:16
    OO00000OO0OOOOO0O ,O00O000O0OOO0OO00 =generate_DOE (O000000OO000OO000 ,OO000OO000OO000O0 )#line:17
    if type (OO00000OO0OOOOO0O )!=int or type (O00O000O0OOO0OO00 )!=int :#line:18
        OOO0000OO0O0OO00O =write_csv (OO00000OO0OOOOO0O ,O00O000O0OOO0OO00 )#line:19
        if OOO0000OO0O0OO00O !=-1 :#line:20
            print ("\n分析输入并构建 DOE...",end =' ')#line:21
            time .sleep (2 )#line:22
            print ("完成...")#line:23
            time .sleep (0.5 )#line:24
            print (f"输出文件: {O00O000O0OOO0OO00}.csv，位于“DOE实验输出”文件夹")#line:25
        else :#line:26
            print ("\n写入输出文件时出错。 \n如果您打开了具有相同文件名的文件，请在再次运行命令之前将其关闭！")#line:27
"""
print ()#line:34
print (" "*5 +"DoE实验设计系统，墨非未已，气体机清洁燃烧团队"+" "*5 )#line:35
print (" "*20 +"June 2024, 吉林长春"+" "*20 )#line:36
print ()#line:37
"""
execute_main ()#line:40
