# def sum(a,b):
#     result=a+b
#     print(result)
# sum(10,20)

# def buy():
#     return 'money'

# a=buy()
# print(a)
#
# def sum(a,b):
#     return a+b
# result=sum(10,20)
# print(return)

# def hanshu (a,b):
#     """qiu'chen'ji"""
# help(hanshu)

# def testB():
#     print('吃饭')
#     print('吃饭')
# def testA():
#     print('睡觉')
#     testB()
#     print('睡觉')
# testA()

# def a():
#     print('_'*20)
# def b(c):
#     for i in range(c):
#         a()
# b(5)

# def sum(a,b,c):
#     return (a+b+c)/3
# aa=sum(7,8,9)
# print(aa)

# def he(a,b):
#     for i in range(a,b):
#         if i==(i//100)**3+((i%100)//10)**3+(i%10)**3:
#             print(f'{i}')
# he(100,1000)


# def zhishu(a,b):
#     result = 0
#     for i in range(a,b):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#             else:
#                 result+=i
#     print(f'{result}')
# zhishu(2,101)

# def jiecheng(a):
#     b=1
#     result=0
#     for i in range(1,a+1):
#         b*=i
#         result+=b
#     print(f'{result}')
# jiecheng(4)

# def chengfa(a,b):
#     for i in range(a,b):
#         for j in range(a,b):
#             if i>=j:
#                 print(f'{i}*{j}={i*j}',end='\t')
#         print()
# chengfa(1,10)

# class A():
#     def __init__(self):
#         self.sum=0
#     def jishu(self,b):
#         for i in range(b+1):
#             if i%2!=0:
#                 self.sum+=i
#         print(self.sum)
# aa=A()
# aa.jishu(100)

# import xlwt
# f=xlwt. Workbook('测试.xls')
# sheet=f.add_sheet('信息表')
# for i in range(1,10):
#     for j in range(1,10):
#         if i>=j:
#             sheet.write(i-1,j-1,f'{j}*{i}={i*j}')
# f.save('测试.xls')

# import xlwt
# with open('ccc.txt','r',encoding='utf-8') as f:
#     aa=f.readlines()
#     ff=xlwt.Workbook()
#     sheet= ff.add_sheet('信息')
#     for i in range(len(aa)):
#         a=aa[i].replace('\n','').split(',')
#         for j in range(len(a)):
#             sheet.write(i,j,a[j])
#     ff.save('信息表.xls')

#将表格中的内容写入到文件中
# import xlrd
# with open('ddd.txt','w',encoding='utf-8')as f:
#     ff=xlrd.open_workbook('信息表.xls')
#     sheet =ff.sheets()[0]
#     for i in range(sheet.nrows):
#         b=','.join(sheet.row_values(i))
#         if i==sheet.nrows-1:
#             f.write(b)
#         else:
#             f.write(b+'\n')

#
# import xlrd
# from xlutils.copy import copy
# with open('ddd.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     ff= xlrd.open_workbook('信息表.xls')
#     sheet=ff.sheets()[0]
#     b=sheet.nrows
#     new_ff=copy(ff)
#     sheet1 = new_ff.get_sheet(0)
#     for i in range(len(a)):
#         c=a[i].replace('\n','').split(',')
#         for j in range(len(c)):
#             sheet1.write (i+b,j,c[j])
#     new_ff.save('信息表.xls')

# class A():
#     def he(self,a,b):
#         result=0
#         for i in range(a,b+1):
#             if i%2!=0:
#                 result+=i
#         return result
#     def c(self,d,e):
#         with open('b.txt','w',encoding='utf-8') as f:
#             f.write(str(self.he(d,e)))
# aa=A()
# aa.c(2,6)

"""
import 模块名  模块名.函数名()
import os
os.listdir()
from 模块名 import *    函数名()
from os import *
os.listdir()
from 模块名 import 函数名   函数名()
from os import listdir
listdir()
import 模块名 as 别名    别名.函数名()
import os as qq
qq.listdir()
from  模块名 import 函数名 as 别名  别名()
from os import listdir as qq
qq()
"""
# f=open('a.txt','w',encoding='utf-8')
# f.write('用魏凯凯永远单身换我小保底必中甘雨')
# f.close()
# with open('a.txt','w',encoding='utf-8')as f:
#     f.write('魏凯凯阿贝多必歪')
# with open('a.txt','r',encoding='utf-8')as f:
#     f.readlines()#不加参数默认全部读取，格式为列表
#     f.readline()#默认值读一行，具有累加功能
#     f.read()#不加参数默认全部读取，格式为字符串
# with open('a.txt','a',encoding='utf-8')as f:
#     f.write('魏凯凯小保底必歪')
# #调用os模块
# import os
# '重命名'
# os.rename()
# '删除文件'
# os.remove()
# '获取目录'
# os.listdir()
# '创建文件夹'
# os.mkdir()
# '删除文件夹'
# os.rmdir()
# '获取当前路径'
# os.getcwd()
# '切换路径'
# os.chdir()
# '添加递归目录'
# os.makedirs()
# '删除递归目录'
# os.removedirs()
# '将路径与文件名分开'
# os.path.split()
# '将路径与文件后缀名分开'
# os.path.splitext()
# '将盘符与路径分开'
# os.path.splitdrive()
# '判断是否是目录'
# os.path.isdir()
# '判断是否是文件'
# os.path.isfile()
# '判断路径下是否存在目录或文件'
# os.path.exists()

# import pymysql
# #连接数据库
# conn=pymysql.connect(host='192.168.10.15',
#                      port=3306,
#                      user='root',
#                      passwd='123456',
#                      charset='utf8')
# abc=conn.cursor()#创建游标控制器
# abc.execute('show databases;')#执行sql语句
# abc.fetchall()#接收上句sql语句产生的结果,接受全部
# abc.fetchany()#接收上句sql语句产生的结果，默认接受一行
# abc.fetchone()#接收上句sql语句产生的结果，每次接收一行，具有累加作用
# conn.commit() #对表内容修改后需要提交才能生效

#xlrd---读取    xlwt---写入    xlutils----追加
# import xlwt
# f=xlwt. Workbook()     #打开一个exce表格
# sheet=f.add_sheet ('信息表')#添加一个标签页，括号里写的是标签页的名字
# sheet.write(0,0,'小明')#给标签页中加入书据，括号里写入行、列、内容
# f.save('软件测试.xls')#保存
#
# import xlrd
# f=xlrd.open_workbook('软件测试.xls')#打开要读取的excel表格
# print(f.nsheets) #获取表格中有多少个标签页
# print(f.sheet_names())#获取表格中每个标签页的名字
# #
# sheet=f.sheets()[0]  #根据索引获取想要操作的标签页
# f.sheet_by_name('信息表')#根据名字获取想要操作的标签页
# #
# print(sheet.nrows)#获取标签页中有多少行内容
# print(sheet.row_values(0))#根据索引获取标签页中某一行内容
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))
# #
# print(sheet.ncols)#获取标签页有多少列内容
# print(sheet.col_values(0))#根据索引获取标签页中某一列内容
# for i in range(sheet.ncols):
#     print(sheet.col_values(i))
#
#     print(sheet.cell(0,1).value)#根据单元格获取某一个元格里的内容

# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('测试.xls') #打开要操作的excel表格
# new_f=copy(f) #将xlrd对象转换为xlwt对象
# sheet =new_f.get_sheet(0)#根据索引获取想要操作的标签页
# sheet.write(3,1,'tom')















































