import requests
from bs4 import BeautifulSoup
import os # 用于文件目录操作

# 教程：https://blog.csdn.net/hzwyjxy/article/details/85164067

# url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx?TestNum=1&SelTestNum=170&SelectTest=yes"
url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx"
# TestNum不知道是什么含义
# SelTestNum表示题目序号
d={'TestNum':'1','SelTestNum':'1','SelectTest':'yes'}

# 头部信息
headers = {
    # 用户标识
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
    # Cookie
    'Cookie':'_ga=GA1.3.1256847576.1601191563; ASP.NET_SessionId=ixi0wac51sgxmbdi4m4pv2fu; iPlanetDirectoryPro=ZbN712VGOA30elEnQByPYg',
    # 报文主体的对象类型
    'content-type': 'application/x-www-form-urlencoded'
}

# post获取网页数据
response=requests.post(url,data=d,headers=headers)
# 打印网页数据(HTML文本)
print(response.text)
# BeautifulSoup是HTML解析器，用于提取信息
# 将html文本转换为文档对象
soup=BeautifulSoup(response.text)
# 打印文档对象
soup
# 提取出id为'trTestTypeContent1'(题目的id='trTestTypeContent'+题目序号)的table标签
QuestionTable=soup.find_all('table',{'id':'trTestTypeContent1'})
# 打印，查看信息
QuestionTable

# 最终成果文本
resultStr=""

# 题目类型 单选题/判断题/多选题
# 找到input标签
str1=QuestionTable[0].find('input')
str1
str1["value"]
# input标签的value属性值记录了题目类型
resultStr=resultStr+str1["value"]+'\n'
resultStr

# 题目、答案和解析
# 找到所有td标签
QuestionStr=QuestionTable[0].find_all('td')
# for i in range(len(test)):
for i in QuestionStr:
    # 如果不是空行，就追加该行
    if(i.text!=''):
        # print(i.text)
        resultStr+=i.text+'\n'
# 打印，查看信息
resultStr

# 打开文件夹
dataFolder=r"D:\00\20200928爬取南京大学实验室安全考试题库"
os.chdir(dataFolder) # 打开文件目录，相当于cd
os.getcwd() # 返回当前工作目录，显示当前文件目录

# 将成果文本写入文本文件
a= open('a.txt','w')
a.write(resultStr)
a.close()
