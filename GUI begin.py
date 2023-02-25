from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import message.
from tkinter import *
from tkinter import ttk
from tkinter import messangebox
#ไปดูเพิ่มเติม

GUI = Tk()#เรียกหน้าจอขึ้นมา
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อโปรแกรม
GUI.geometry('500x400')#ขนาดหน้าจอ

B1 = ttk.Button(GUI,text ='เงินมีอยู่กี่บาท')
B1.pack(ipadx = 20, ipady=20)

#ชื่อโปรแกรมที่เราตั้ง
L1 = Label(GUI,text= 'โปรแกรมบันทึกความรู้' ,font= ('Angsana New',30),fg=('green'))
L1.place(x=30,y=20)
####################################


def  Button2():
    text = 'ตอนนี้มีเงินในบัชชีอยู่300'
    messagebox.showinfo('เงินในบัชชี',text)



FB1 = Frame(GUI) #คล้่่ายกระดาน
FB1.place(x=200,y=200)
B1 = ttk.Button(FB1,text ='เงินมีอยู่กี่บาท',command=Button2)
B1.pack(ipadx=20 ,ipady=20)#กำหนดโลเคชั่น

def  Button3():
    text = 'คุณได้รับเงิน100บาท'
    messagebox.showinfo('คุณได้รับข้อความ',text)


FB1 = Frame(GUI) #คล้่่ายกระดาน
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text ='คุณได้รับเงิน100บาท',command=Button2)
B2.pack(ipadx=20 ,ipady=20)#กำหนดโลเคชั่น



#ไปเขียนต่อ เพิ่มเติม ในอื่นๆด้วย

GUI.mainloop()
