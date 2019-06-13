# 본인의 과제명 작성

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학부 |201424559 |황보규민


## 프로젝트 개요
파이썬으로 공공데이터를 활용한 휴게소종합정보 제공 서비스
[발표자료](https://github.com/ghkdqhrbals/computerSystem/blob/master/%EC%BB%B4%EC%8B%9C%EC%9E%85%EA%B8%B0%EB%A7%90%EB%B0%9C%ED%91%9C201424559.pptx)
1. input창에 자신이 원하는 고속도로 입력
2. 정보 출력

 
 
 
 
 
  
  
  
  
  기간


  
  
  개요


  
  
  상세설명


  
 
 
  
  sprint 1


  
  
  4.30~5.6


  
  
  공공데이터 받아오기


  
  
  www.data.go.kr에 접속한 뒤 전국 고속도로 휴게소 표준 데이터 csv파일 다운 및 파이썬에 적용


  
 
 
  
  sprint 2


  
  
  5.6~5.13


  
  
  Pandas 설치
  및 csv파일 정리


  
  
  파이썬 데이터 모듈 pandas를 pip로
  설치 한 뒤, 공공데이터 csv파일을 읽고 필요한 column을 추출.


  
 
 
  
  sprint 3


  
  
  5.13~5.20


  
  
  tkinter그래픽
  모듈 사용


  
  
  내장되있는 tkinter
  그래픽 모듈을 사용해 window창에 학번이름,
  휴게소 정보,
  input text 구현


  
 
 
  
  sprint 4


  
  
  5.20~5.27


  
  
  정보 찾기 함수 구현


  
  
  window 창에 input
  text에 따른 string값을 받아와 휴게소 정보를 찾는 find
  함수 구현


  
 
 
  
  sprint 5


  
  
  5.27~6.4


  
  
  기말보고서 착수


  
  
  기말 보고서 착수.


  
 


## 사용한 공공데이터 
[데이터보기](https://github.com/ghkdqhrbals/computerSystem/blob/master/3.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/ghkdqhrbals/computerSystem/blob/master/201424559_황보규민.py) 

* 코드 삽입
import pandas as pd
import tkinter as tk
import tkinter.font
import csv

df = pd.read_csv('3.csv',sep=",",dtype='unicode',encoding = 'utf-8')

df2 = df[["휴게소명","도로종류","매점유무"]]


window=tkinter.Tk()

def find(event):
    strg = str(entry.get())
    df4=df[df['휴게소명']==strg]
    df3 = df4[['휴게소명','도로종류','도로노선번호','도로노선명','도로노선방향','도로점용면적']]
    df5 = df4[['위도','경도','휴게소종류','휴게소운영시작시각','휴게소운영종료시각']]
    df6 = df4[['주차면수','경정비가능여부','주유소유무','LPG충전소유무','전기차충전소유무','버스환승가능여부']]
    df7 = df4[['쉼터유무','화장실유무','약국유무','수유실유무','매점유무','음식점유무']]
    df8 = df4[['기타편의시설','휴게소대표음식명','휴게소전화번호','데이터기준일자','제공기관코드','제공기관명']]

    str(df3)
    print(df3)

    label.config(text=df3)
    label2.config(text=df5)
    label3.config(text=df6)
    label4.config(text=df7)
    label5.config(text=df8)
def countUP():
    global count
    count += 1
    label.config(text=str(count))
def calc(event):
    label.config(text="결과="+str(eval(entry.get())))

window.title("전국 고속도로정보")
window.geometry("900x500+100+100")
window.resizable(False, True)

font = tkinter.font.Font(family="맑은 고딕", size=20 )
font2 = tkinter.font.Font(family="맑은 고딕", size=10)

label =tkinter.Label(window,text="컴퓨터시스템입문 기말과제",relief="solid",font=font)
label.pack()
label =tkinter.Label(window,text="201424559 황보규민",width=640,anchor="e")
label.pack()
label =tkinter.Label(window,text="고속도로이름 입력.",height=4,width=640,anchor="s",font=font2, fg="blue" )
label.pack()

entry=tkinter.Entry(window)
entry.bind("<Return>",find)
entry.pack()

count =0


label = tkinter.Label(window,text="")
label.pack()

label2 = tkinter.Label(window,text="")
label2.pack()

label3 = tkinter.Label(window,text="")
label3.pack()

label4 = tkinter.Label(window,text="")
label4.pack()

label5 = tkinter.Label(window,text="")
label5.pack()






window.mainloop()

##infile = codecs.open('final2.csv','r',encoding='utf-8')

##for line in infile:


##infile.close()
