'''
@Author: your name
@Date: 2020-03-16 11:12:27
@LastEditTime: 2020-03-18 21:29:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import requests
# # 借助BeautifulSoup包解析
from bs4 import BeautifulSoup
# import re #使用正则表达式库,可以用这个库实现字符串片段匹配
import os # 用于文件目录操作
# import shutil # 用于文件目录的高级操作

headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
    'Cookie':'_ga=GA1.3.1256847576.1601191563; ASP.NET_SessionId=ixi0wac51sgxmbdi4m4pv2fu; iPlanetDirectoryPro=ZbN712VGOA30elEnQByPYg',
    'content-type': 'application/x-www-form-urlencoded'
    # 'content-type': 'content-type: text/html; charset=UTF-8'
}

resultStr=""
for i in range(1, 1041):
    print(i)
    # url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx?TestNum=1&SelTestNum=170&SelectTest=yes"
    url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx"
    # TestNum表示类别
    d={'TestNum':'3','SelTestNum':'','SelectTest':'yes'}
    d['SelTestNum']=str(i)
    response=requests.post(url,data=d,headers=headers)
    soup=BeautifulSoup(response.text)
    # soup
    idStr='trTestTypeContent'+str(i)
    # QuestionTable=soup.find_all('table',{'id':'trTestTypeContent1040'})
    QuestionTable=soup.find_all('table',{'id':idStr})
    # QuestionTable

    
    # 题目类型 单选题/判断题/多选题
    resultStr=resultStr+'题目类型：'+QuestionTable[0].find('input')["value"]+'\n'

    # 题目、答案和解析
    QuestionStr=QuestionTable[0].find_all('td')
    # for i in range(len(test)):
    for i in QuestionStr:
        if(i.text!=''):
            # print(i.text)
            resultStr+=i.text+'\n'
    resultStr+='\n'


resultStr


dataFolder=r"D:\00\20200928爬取南京大学实验室安全考试题库"
os.chdir(dataFolder) # 打开文件目录，相当于cd
os.getcwd() # 返回当前工作目录，显示当前文件目录

a= open('a.txt','w',encoding='UTF-8')
a.write(resultStr)
a.close()
