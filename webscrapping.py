import requests
from bs4 import BeautifulSoup
from notify_run import Notify
from datetime import datetime
import time
import smtplib
from twilio.rest import TwilioRestClient as Call


URL="https://www.amazon.in/Test-Exclusive-607/dp/B07HGJKDQB/ref=sr_1_1?crid=2PPNPDG0PHHJ1&keywords=oneplus+7+pro+mobile&qid=1570414247&smid=A23AODI1X2CEAE&sprefix=one+%2Caps%2C330&sr=8-1"

myprice=54000
pnmsg="takkuvaki vastundi ra babu"

headers={"User-Agent":'Mozilla/5.0'}
def price():
	page=requests.get(URL, headers=headers)
	soup=BeautifulSoup(page.content,'html.parser')
	title=soup.find(id="productTitle").get_text()
	price=soup.find(id="priceblock_ourprice").get_text()
	price_main=price[2:]
	print (price_main)
	print(title.strip())
	print(price)
	l=len(price_main)
	if l<=6 :
		price_main=price[2:5]
	else:
		l1=price[2:4]
		l2=price[5:8]
		l3=str(l1)+str(l2)
		price_main=int(l3)
	price_now=int(price_main)
	print(price_now)
	name=str(title.strip())

	i=0;
	if(price_now <= myprice):
		mail()
		notify()
		call()
	else:
		i=i+1
		print("last checked at "+str(datetime.now()))


def mail():
	h=smtplib.SMTP_SSL('smtp.gmail.com',465)
	h.ehlo()
	h.ehlo()
	print("ss")
	h.login('type ur email','type ur password')
	subject="dabbulu taggayi ra babu"
	body="dabbulu taggayi fast ga konu ra.E link open chey"+URL
	msg = f"Subject: {subject} \n\n {body} "
	h.sendmail('type ur email','type email to which u have to send',msg)
	print("babu mail poyindi")
	h.quit()
def notify():
	k=Notify()
	k.send("see ra")
	print("bro notification push ayindi")
	#print("oka araganta aagi ra po")
d=0;
while(True):
	d=d+1
	print("d:"+str(d))
	price()
	time.sleep(10)	
def call():
	from_no="+19065534095"
	to="+917981538116"
	client=Call("AC841628bbef609de97073ede3a05d22a7","2eb87ea4af9f6c58364891c2e163c530")
	src="https://demo.twilio.com/docs/voice.xml"
	print('call initiated')
	client.calls.create(to=to,from_=from_no,url=src,method='GET')
	print ('Call started')	
		
				
	
		
