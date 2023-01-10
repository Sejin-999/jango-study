import smtplib
import json
import pymysql
import requests
from parse import *
from email.mime.text import MIMEText

#exParam = requests.get("http://127.0.0.1:8000", params={"email" : "1106q@naver.com" , "orderbillid" : "1"})
#print(exParam.text)
context = "TEST 입니다"

# json setting Start
exJson = '{"email" : "1106q@naver.com" , "orderbillid" : "1"}'

#mail setting Start
def appleMailSetting(exJson):
    #setting start
    global email , subject , orderbillid
    loadsJson = json.loads(exJson)
    email = loadsJson["email"]
    orderbillid = loadsJson["orderbillid"]
    #setting end
    
    # parshing start
    idparse = parse("{}@naver.com",email)
    subject = idparse[0]+"님 구매 감사합니다!"
    # parshing end
    
    # Test code start
    print(exJson)
    print("제목 : "+subject + "\n이메일 : "+email +"\n오더 아이디 : "+orderbillid) 
    # Test code end
#mail setting End

#json setting end

#orderbillid 를 통한 content 가져오기 Start
#TODO
#dbconnect Start
def dbcon():
    db = pymysql.Connect(host='localhost' ,user="root" , password="1234", database="heyAppledb")
    cursor = db.cursor()

    query="select * from FruitOrderBill"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
#dbconnect End


#Total price 
#fruit name -> count & price  
#orderbillid 를 통한 content 가져오기 End

#mail Send Start
def appleMail(email , context):
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login('testproject9197@gmail.com','joilxdqyvpihtlkf')


    msg = MIMEText(context)
    msg['Subject'] = subject

    smtp.sendmail('testproject9197@gmail.com',email,msg.as_string())

    smtp.quit()    
#mail Send End
# 함수실행 줄 Start
#appleMailSetting(exJson)
#appleMail(email ,context)
# 함수실행 줄 End

# check value Start
#print(subject)
# check value End
