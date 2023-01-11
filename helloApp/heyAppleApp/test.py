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
    global subject
    loadsJson = json.loads(exJson)
    email = loadsJson["email"]
    orderbillid = loadsJson["orderbillid"]
    #setting end
    
    # parshing start
    idparse = parse("{}@naver.com",email)
    subject = idparse[0]+"님 구매 감사합니다!"
    # parshing end
    '''
    # Test code start
    print(exJson)
    print("제목 : "+subject + "\n이메일 : "+email +"\n오더 아이디 : "+orderbillid) 
    # Test code end
    '''
    dbcon(email,orderbillid)
#mail setting End

#json setting end

#orderbillid 를 통한 content 가져오기 Start
#TODO
#dbconnect Start
def dbcon(email,orderbillid):
    email = email
    print("dbcon orderbillID : "+orderbillid) #오더아이디가 잘넘어왔나요?
    #global totalPrice , fruitName , count
    global saveInfo
    db = pymysql.Connect(host='localhost' ,user="root" , password="1234", database="heyAppledb")
    cursor = db.cursor()

    query="select total_price from OrderBill where id ="+orderbillid #Total price
    cursor.execute(query)
    result = cursor.fetchone() #result는 tuple 임 ... 배열로 값들이 들어와있어서 꺼낼때 한번더 꺼내주기
    totalPrice = result[0]
    #print(totalPrice)
    
    query2="select Distinct fruit_id , count from FruitOrderBill where orderbill_id =1" #fruit_id & count 
    cursor.execute(query2)
    result = cursor.fetchall()
    #print("투플사이즈:",len(result))
    saveInfo= [[0 for col in range(3)] for row in range(len(result))] #col 열 row 행
    
    flag = 0
    
    for i ,k in result:
        count = k
        #print("Fruit id : ",i , "   count : ", k)
        
        #Fruit name , price 조회 start
        query3 = "select name , price from Fruit where id ="+str(i)
        cursor.execute(query3)
        results= cursor.fetchall()
        saveInfo[flag][2] =  count
        #print("\n\n")
        
        for i , j in results:
            name =i
            price = j
            saveInfo[flag][0] = name
            saveInfo[flag][1] = price
            flag +=1
            #print("fruit name : ",i ,"fruit price : ",j,"\n")
            #print("최종 저장용 - ","이름 :", name ,"가격 : ",price ,"갯수 : ", count)
            #two_d = [list(map(str,saveInfo)) for _ in range(len(result))]
        #Fruit name , price 조회 end
    #print(saveInfo)
    appleMail(email ,saveInfo)
#dbconnect End

#Total price 
#fruit name -> count & price  
#orderbillid 를 통한 content 가져오기 End

#mail Send Start
def appleMail(email , saveInfo):
    context
    for i in range(len(saveInfo)):
        for j in range(len(saveInfo[i])): # name , price , count
            print(saveInfo[i][j])
            
        print()
    print(context)
    '''
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login('testproject9197@gmail.com','joilxdqyvpihtlkf')


    msg = MIMEText(context)
    msg['Subject'] = subject
    msg['From']= "hey,Apple"

    smtp.sendmail('testproject9197@gmail.com',email,msg.as_string())

    smtp.quit()  
    '''

#mail Send End
# 함수실행 줄 Start
appleMailSetting(exJson)
# 함수실행 줄 End

# check value Start
#print(subject)
#print(orderbillid)
# check value End
'''
#range code
for i in range(len(results)):
for j in range(len(results[i])): # name , price , count
        print(results[i][j])
saveInfo = [results[i] , k] 
print(saveInfo)
print()
'''