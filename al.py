from tkinter.ttk import*
from tkinter import*

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime, date
from time import sleep
from threading import Thread
from tkinter import messagebox 

bg_color="#ffffff"
fline_col="#F78F8F"

x=Tk()
x.title('Alarm Clock ')
x.geometry('700x350')
x.configure(bg=bg_color)

frame_line = Frame(x, width=900, height=6, bg = fline_col)
frame_line.grid(row=0, column=0)

frame_body=Frame(x, width=900, height=400,bg='#B0C1D4')
frame_body.grid(row=1,column=0)

img= Image.open('alarm.png ')
img.resize((200,200))
img=ImageTk.PhotoImage(img)

app_image=Label(frame_body,height=100,image=img,bg='#B0C1D4')
app_image.place(x=40,y=40)

name=Label(frame_body,text='Alarm' , height=1,font=('cursive 18 bold'),fg='#AD1414',bg='#B0C1D4')
name.place(x=290,y=40)

hour=Label(frame_body,text='hour' , height=1,font=('ivy 10 bold'),fg='#AD1414',bg='#B0C1D4')
hour.place(x=252,y=90)
c_hour=Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
c_hour.current(0)
c_hour.place(x=245,y=120)


min=Label(frame_body,text='minute' , height=1,font=('ivy 10 bold'),fg='#AD1414',bg='#B0C1D4')
min.place(x=322,y=90)
c_min=Combobox(frame_body,width=2,font=('arial 15'))
c_min['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',
'31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
c_min.current(0)
c_min.place(x=325,y=120)

sec=Label(frame_body,text='second' , height=1,font=('ivy 10 bold'),fg='#AD1414',bg='#B0C1D4')
sec.place(x=412,y=90)
c_sec=Combobox(frame_body,width=2,font=('arial 15'))
c_sec['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',
'31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
c_sec.current(0)
c_sec.place(x=415,y=120)

period=Label(frame_body,text='period' , height=1,font=('ivy 10 bold'),fg='#AD1414',bg='#B0C1D4')
period.place(x=492,y=90)
c_period=Combobox(frame_body,width=3,font=('arial 12'))
c_period['values']=('AM','PM')
c_period.current(0)
c_period.place(x=495,y=120)

day=Label(frame_body,text='day' , height=1,font=('ivy 12 bold'),fg='#AD1414',bg='#B0C1D4')
day.place(x=60,y=160)
c_day=Combobox(frame_body,width=4,font=('arial 12'))
c_day['values']=('select ','Sun','Mon','Tue','Wed','Thu','Fri','Sat')
c_day.current(0)
c_day.place(x=60,y=190)

date=Label(frame_body,text='date', height=1, font=('ivy 12 bold') ,fg='#AD1414',bg="#B0C1D4")
date.place(x=90,y=160)
c_date=Entry(frame_body,width=20,bg="#B0C1D4",borderwidth=3,fg="#AD1414")
c_date.place(x=150,y=190)
c_date.insert(0,"DD-MM-YY : ")


def activate():
	t=Thread(target=alarm)
	t.start()



def deactivate():
	mixer.music.stop()



selected=IntVar()

rad1=Radiobutton(frame_body,font=('arial 10 bold'), value=1, text='Activate',bg='#B0C1D4',fg='#AD1414',command=activate,variable=selected)
rad1.place(x=210,y=230)

def sound_alarm():
	mixer.music.load('alarm.mp3')
	mixer.music.play()

	rad2 = Radiobutton(frame_body,font=('arial 10 bold'), value=2, text='Deactivate',bg='#B0C1D4',fg='#AD1414',command=deactivate,variable=selected)
	rad2.place(x=290,y=230)
   

#Tk().withdraw() # to avoid showing the root window


def alarm():
	while True:
		control=1
		alrm_hr = c_hour.get()
		alrm_min = c_min.get()
		alrm_sec = c_sec.get()
		alrm_period = (c_period.get()) .upper()
		alrm_day = c_day.get()
		alrm_date = c_date.get()

		now=datetime.now()
		hr = now.strftime('%I')
		min = now.strftime('%M')
		sec= now.strftime('%S')
		period = now.strftime('%p')
		day = now.strftime('%a')
		date = now.strftime('%d-%m-%Y')

		if control == 1:
			if  alrm_period == period and alrm_hr == hr and alrm_min == min and alrm_sec == sec :
				if alrm_day == day and alrm_date == date :
					sound_alarm()
					messagebox.showinfo(title="Message",message="Remainder")
					
		sleep(1)





mixer.init()
				

x.mainloop()