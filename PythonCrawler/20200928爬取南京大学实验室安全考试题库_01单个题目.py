import requests
from bs4 import BeautifulSoup
import os # 用于文件目录操作

# url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx?TestNum=1&SelTestNum=170&SelectTest=yes"
url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx"
d={'TestNum':'1','SelTestNum':'1','SelectTest':'yes'}
headers = {
    # 用户标识
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
    # Cookie
    'Cookie':'_ga=GA1.3.1256847576.1601191563; ASP.NET_SessionId=ixi0wac51sgxmbdi4m4pv2fu; iPlanetDirectoryPro=ZbN712VGOA30elEnQByPYg',
    # 报文主体的对象类型
    'content-type': 'application/x-www-form-urlencoded'
}

response=requests.post(url,data=d,headers=headers)
print(response.text)

soup=BeautifulSoup(response.text)
soup
QuestionTable=soup.find_all('table',{'id':'trTestTypeContent1040'})
QuestionTable

str=""

# 题目、答案和解析
test=QuestionTable[0].find_all('td')
# for i in range(len(test)):
for i in  test:
    if(i.text!=''):
        # print(i.text)
        str+=i.text+'\n'
str

# 题目类型 单选题/判断题/多选题
str1=QuestionTable[0].find('input')
str1
str1["value"]
str=str+str1["value"]+'\n'
str

dataFolder=r"D:\00\20200928爬取南京大学实验室安全考试题库"
os.chdir(dataFolder) # 打开文件目录，相当于cd
os.getcwd() # 返回当前工作目录，显示当前文件目录

a= open('a.txt','w')
a.write(str)
a.close()
