import pytesseract , re , sys
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.3.0/bin/tesseract'


def printRes():
    a = Image.open('rec2.jpg')
    result = pytesseract.image_to_string(a) #lang='kor' 한국어
    global res 
    res = result.split()
    resNum = re.sub(r'[^0-9]','',result)
    print(res)
    print("숫자만 보기")
    print(resNum)
    print("하나씩꺼내기")

def printResSave():
    print("파일로 값저장하기 시작")
    sys.stdout = open('stdoutb.txt' , 'w')

    for i in res:
        print(i)

    sys.stdout.close()    

printRes()







