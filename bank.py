from tkinter import *
wd=Tk()
wd.geometry('600x600')
d=list()
destroy=0
deposite=0
withdrawal=0
created=0
pasw1=''
acc1=''
pasw1=''
def newacc():
	global lblt,btn,lbl,frm,e,destroy,created
	for i in range(0,3):
		btn[i].destroy()
		lbl[i].destroy()
	lbl[3].destroy()
	if created==1:
		lbl[4].destroy()
	if destroy==1:	
		lblt.destroy()
	show()
def save():
	global lblt,destroy,btn,lbl,frm,e,created
	created=0
	if destroy==1:
		lblt.destroy()
		destroy=0
	acc=e[0].get()
	pasw=e[1].get()
	name=e[2].get()
	e[0].delete(0,END)
	e[1].delete(0,END) 
	e[2].delete(0,END)
	if acc=='' or pasw=='':
		return
	file=open('back.txt','r')
	words=['']*2
	for line in file:
		words=line.split()
		if words==[]:
			break
		if words[1]==acc:
			lblt=Label(wd,text='Acc No. Already Exist!',font=('bold',20),background='light blue',width=35,fg='red')
			lblt.place(x=1,y=168)
			destroy=1			
			return
	file=open('back.txt','a')
	file.write(name)
	file.write(' ')
	file.write(acc)
	file.write(' ')
	file.write(pasw)
	file.write(' ')
	file.write('0')
	file.write('\n')
	file.close()
	start()
def amount():
	global acc1,name1,pasw1,destroy,e,deposite,withdrawal
	global lblt,btn,lbl,frm,e,created	
	money=int(e[0].get())		
	e[0].delete(0,END)
	lbl[0].destroy()
	e[0].destroy()
	btn[0].destroy()
	btn[1].destroy()
	lines=0
	words=[[]*4]*100
	file=open('back.txt','r')
	for line in file:
		words[lines]=line.split()
		if words[lines][1]==acc1:
			if deposite==1:
				lblt=Label(wd,text='You Deposit Rupees '+str(money),font=('bold',18),background='light blue',width=40,fg='green')
				lblt.place(x=1,y=200)
				money=money+int(words[lines][3])
				deposite=0
			if withdrawal==1:	
				if money<=int(words[lines][3]):
					money=int(words[lines][3])-money
					lblt=Label(wd,text='You Withdraw Rupees '+str(money),font=('bold',18),background='light blue',width=40,fg='green')
					lblt.place(x=1,y=200)
				else:
					money=int(words[lines][3])
					lblt=Label(wd,text='Not Enough Money',background='light blue',width=40,fg='red',font=('bold',18))
					lblt.place(x=1,y=200)	
				withdrawal=0			
			destroy=1
			words[lines][3]=str(money)		
		lines+=1	
	file.close()	
	file=open('back.txt','w')
	for line in range(0,lines):
		for i in range(0,4):
			file.write(words[line][i])
			file.write(' ')
		file.write('\n')	
	file.close()
	lblt=Label(wd,text='Your Balance is '+str(money),background='light blue',width=35,fg='red',font=('bold',20))
	lblt.place(x=1,y=240)
	btn[0]=Button(wd,text='Back',font=('italic',15),width=6,height=2,command=start)
	btn[0].place(x=1,y=285)
	btn[1]=Button(wd,text='Exit',font=('italic',15),width=6,height=2,command=exit)
	btn[1].place(x=491,y=285)
	money=0		
def deposit():
	global lblt,destroy,btn,lbl,frm,e,created,deposite
	deposite=1
	btn[0].destroy()
	btn[1].destroy()
	btn[2].destroy()
	lblt.destroy()
	lblt=Label(wd,text='Enter Deposit Amount',background='light blue',width=40,fg='red',font=('bold',18))
	lblt.place(x=1,y=200)	
	lbl[0]=Label(wd,text='Enter Amount',font=('bold',15),background='gray',fg='black',width=11,anchor=W)
	lbl[0].place(x=1,y=250)	
	e[0]=Entry(wd,font=('helvetica',15),width=40)
	e[0].place(x=152,y=250)
	btn[0]=Button(wd,text='Proceed',font=('italic',15),width=6,height=2,command=amount)
	btn[0].place(x=491,y=285)
	btn[1]=Button(wd,text='Back',font=('italic',15),width=6,height=2,command=lambda n=name1,a=acc1,pa=pasw1:trans(n,a,pa))
	btn[1].place(x=1,y=285)
def withdraw():
	global lblt,destroy,btn,lbl,frm,e,created,withdrawal
	withdrawal=1
	btn[0].destroy()
	btn[1].destroy()
	btn[2].destroy()
	lblt.destroy()	
	lblt=Label(wd,text='Enter Withdraw Amount',background='light blue',width=40,fg='red',font=('bold',18))
	lblt.place(x=1,y=200)
	lbl[0]=Label(wd,text='Enter Amount',font=('bold',15),background='gray',fg='black',width=11,anchor=W)
	lbl[0].place(x=1,y=250)	
	e[0]=Entry(wd,font=('helvetica',15),width=40)
	e[0].place(x=152,y=250)
	btn[0]=Button(wd,text='Proceed',font=('italic',15),width=6,height=2,command=amount)
	btn[0].place(x=491,y=285)
	btn[1]=Button(wd,text='Back',font=('italic',15),width=6,height=2,command=lambda n=name1,a=acc1,pa=pasw1:trans(n,a,pa))
	btn[1].place(x=1,y=285)
def trans(n,a,pa):
	global lblt,destroy,btn,lbl,frm,e,created,name1,acc1,pasw1
	name1=n
	acc1=a
	pasw1=pa
	for i in range(0,3):
		btn[i].destroy()
		lbl[i].destroy()
	lbl[3].destroy()
	e[0].destroy()
	e[1].destroy()
	if created==1:
		lbl[4].destroy()
		created=0
	if destroy==1:	
		lblt.destroy()
		destroy=0
	lbl[0]=Label(wd,text='Bank Of',font=('bold',20),background='light blue',width=35,fg='Dark blue')
	lbl[0].place(x=1,y=30)
	lbl[1]=Label(wd,text='SK',font=('bold',20),background='light blue',width=35,fg='Dark blue')
	lbl[1].place(x=1,y=70)	
	lblt=Label(wd,text='Hello '+name1+'!',font=('bold',20),background='light blue',width=35,fg='black')
	lblt.place(x=1,y=150)
	lblt=Label(wd,text='Please Choose Your Service?',font=('bold',20),background='light blue',width=35,fg='red')
	lblt.place(x=1,y=230)	
	btn[1]=Button(wd,text='Deposit',fg='green',font=('italic',15),width=6,height=2,command=deposit)
	btn[1].place(x=491,y=317)
	btn[0]=Button(wd,text='Back',fg='red',font=('italic',15),width=6,height=2,command=start)
	btn[0].place(x=250,y=317)
	btn[2]=Button(wd,text='Withdraw',fg='blue',font=('italic',15),width=6,height=2,command=withdraw)
	btn[2].place(x=1,y=317)
	destroy=1	
def	proceed():
	global lblt,destroy,e
	if destroy==1:
		lblt.destroy()
		destroy=0
	acc=e[0].get()
	pasw=e[1].get()
	e[0].delete(0,END)
	e[1].delete(0,END)
	file=open('back.txt','r')
	words=['']*2
	for line in file:
		words=line.split()
		if words==[]:
			return	
		if words[1]==acc and words[2]==pasw:
			name=words[0]
			trans(name,acc,pasw)	
			return
	lblt=Label(wd,text='Try Again!',font=('bold',20),background='light blue',width=35,fg='red')
	lblt.place(x=1,y=200)
	destroy=1
def close():
	exit()
lblt=''	
frm=['']*1
lbl=['']*5
btn=['']*3
e=['']*3
lble=''
def show():
	global lblt,btn,lbl,frm,e,created,lble
	created=1
	frm=Frame(wd,background='light blue',height=600,width=600)
	frm.place(x=0,y=0)
	lblt=Label(wd,text='Enter Detail For New Account',font=('bold',18),background='light blue',width=40,fg='red')
	lblt.place(x=1,y=180)
	lbl[0]=Label(wd,text='Bank Of',font=('bold',20),background='light blue',width=35,fg='Dark blue')
	lbl[0].place(x=1,y=30)
	lbl[1]=Label(wd,text='SK',font=('bold',20),background='light blue',width=35,fg='Dark blue')
	lbl[1].place(x=1,y=70)
	lbl[2]=Label(wd,text='Account No.',font=('bold',15),background='gray',fg='Black',anchor=W,width=10)
	lbl[2].place(x=1,y=250)
	lbl[3]=Label(wd,text='Password',font=('bold',15),background='gray',fg='black',width=10,anchor=W)
	lbl[3].place(x=1,y=282)
	lbl[4]=Label(wd,text='Name',font=('bold',15),background='gray',fg='black',width=10,anchor=W)
	lbl[4].place(x=1,y=218)
	e[2]=Entry(wd,font=('helvetica',15),width=41)
	e[2].place(x=139,y=218)
	e[0]=Entry(wd,font=('helvetica',15),width=41)
	e[0].place(x=139,y=250)
	e[1]=Entry(wd,font=('helvetica',15),width=41)
	e[1].place(x=139,y=282)
	btn[1]=Button(wd,text='Save Acc.',font=('italic',15),width=6,height=2,command=save)
	btn[1].place(x=491,y=317)
	btn[0]=Button(wd,text='Back',font=('italic',15),width=6,height=2,command=start)
	btn[0].place(x=250,y=317)
	btn[2]=Button(wd,text='Close',font=('italic',15),width=6,height=2,command=close)
	btn[2].place(x=1,y=317)
def start():
	global lblt,btn,lbl,frm,e,created,lble,destroy
	if created==1:
		for i in range(0,3):
			btn[i].destroy()
			lbl[i].destroy()
		lbl[3].destroy()
		lbl[4].destroy()
		created=0	
	frm=Frame(wd,background='light blue',height=600,width=600)
	frm.place(x=0,y=0)
	lbl[0]=Label(wd,text='Bank Of',font=('bold',20),background='light blue',width=35,fg='Dark blue')
	lbl[0].place(x=1,y=30)
	lbl[1]=Label(wd,text='SK',font=('bold',20),background='light blue',width=35,fg='Dark blue')
	lbl[1].place(x=1,y=70)
	lbl[2]=Label(wd,text='Account No.',font=('bold',15),background='gray',fg='Black',anchor=W,width=10)
	lbl[2].place(x=1,y=250)
	lbl[3]=Label(wd,text='Password',font=('bold',15),background='gray',fg='black',width=10,anchor=W)
	lbl[3].place(x=1,y=282)
	e[0]=Entry(wd,font=('helvetica',15),width=41)
	e[0].place(x=139,y=250)
	e[1]=Entry(wd,font=('helvetica',15),width=41)
	e[1].place(x=139,y=282)
	btn[1]=Button(wd,text='Proceed',font=('italic',15),width=6,height=2,command=proceed)
	btn[1].place(x=491,y=317)
	btn[0]=Button(wd,text='New Acc.',font=('italic',15),width=6,height=2,command=newacc)
	btn[0].place(x=250,y=317)
	btn[2]=Button(wd,text='Close',font=('italic',15),width=6,height=2,command=close)
	btn[2].place(x=1,y=317)
start()	
wd.mainloop()