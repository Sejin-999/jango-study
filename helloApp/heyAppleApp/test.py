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
def dbcon(Orderbillid):
    print("dbcon orderbillID : "+Orderbillid) #오더아이디가 잘넘어왔나요?
    global totalPrice , fruitName , count
    db = pymysql.Connect(host='localhost' ,user="root" , password="1234", database="heyAppledb")
    cursor = db.cursor()

    query="select total_price from OrderBill where id ="+orderbillid #Total price
    cursor.execute(query)
    result = cursor.fetchone() #result는 tuple 임 ... 배열로 값들이 들어와있어서 꺼낼때 한번더 꺼내주기
    totalPrice = result[0]
    print(totalPrice)
    
    query2="select Distinct fruit_id , count from FruitOrderBill where orderbill_id =1" #fruit_id & count 
    cursor.execute(query2)
    result = cursor.fetchall()
    for i in result:
        print(i)
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
appleMailSetting(exJson)
dbcon(orderbillid)
#appleMail(email ,context)
# 함수실행 줄 End

# check value Start
#print(subject)
#print(orderbillid)
# check value End
