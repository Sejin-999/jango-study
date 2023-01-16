from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def abtest():

    msg = MIMEMultipart()
    msg['Subject'] = "테스트"
    msg['From'] = "testproject9197@gmail.com"
    msg['To'] = "1106q@naver.com"

    content = """
        <html>
        <body>
            <h2>{title}</h2>
            <p>메일 전송 테스트입니다</p>
        </body>
        </html>
    """.format(
    title = '메일.. 받으셨나요..?'
    )

    mimetext = MIMEText(content,'html')
    msg.attach(mimetext)

    email_id = '네이버 id'
    email_pw = '네이버 비밀번호'

    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()

    smtp.login('testproject9197@gmail.com','joilxdqyvpihtlkf')
    smtp.sendmail(msg['From'],'testproject9197@gmail.com',msg.as_string())
    smtp.quit()