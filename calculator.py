import tkinter
from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    value_input.set(operator)
def btnclear():
    global operator
    operator=""
    value_input.set("")
def btnEquals():
        global operator
        sumup = str(eval(operator))
        value_input.set(sumup)
        operator=""
def btnDelete():
        value_input.set(value_input.get()[:-1])
Calculator=tkinter.Tk()
Calculator.geometry("240x362")#set the height and width of the window(widthXheight)
Calculator.resizable(0,0)#resizalbe () method is used to create a fixed size window,so that the window can't be change
Calculator.title("Calculator")
operator=""
value_input=StringVar()
display=Entry(Calculator,font=('Times 18',13,'bold'),textvariable=value_input,
bd=30,insertwidth=3,bg="lightcyan",justify='right').grid(columnspan=4)
input_bottonclear=Button(Calculator,padx=2,pady=4,bd=3,fg='black',
font=('black',16,'bold'),text="C",command=btnclear)
input_bottonclear.grid(row=1,column=0)
input_bottondelete=Button(Calculator,padx=0,pady=4.5,bd=3,fg='black',
    font=('black',14,'bold'),text="⌫",command=btnDelete)
input_bottondelete.grid(row=1,column=1)
input_bottonmodule=Button(Calculator,padx=1,pady=4,bd=3,fg='black',
    font=('black',16,'bold'),text="%",command=lambda:btnclick('%'))
input_bottonmodule.grid(row=1,column=2)
input_bottondiv=Button(Calculator,padx=5,pady=3,bd=3,fg='black',
    font=('black',17,'bold'),text="/",command=lambda:btnclick('/'))
input_bottondiv.grid(row=1,column=3)
input_botton7=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="7",command=lambda:btnclick(7))
input_botton7.grid(row=2,column=0)
input_botton8=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="8",command=lambda:btnclick(8))
input_botton8.grid(row=2,column=1)
input_botton9=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="9",command=lambda:btnclick(9))
input_botton9.grid(row=2,column=2)
input_bottonMul=Button(Calculator,padx=4,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="*",command=lambda:btnclick("*"))
input_bottonMul.grid(row=2,column=3)
input_botton4=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="4",command=lambda:btnclick(4))
input_botton4.grid(row=3,column=0)
input_botton5=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="5",command=lambda:btnclick(5))
input_botton5.grid(row=3,column=1)
input_botton6=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="6",command=lambda:btnclick(6))
input_botton6.grid(row=3,column=2)
input_bottonsub=Button(Calculator,padx=4,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="-",command=lambda:btnclick("-"))
input_bottonsub.grid(row=3,column=3)
input_botton1=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="1",command=lambda:btnclick(1))
input_botton1.grid(row=4,column=0)

input_botton2=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="2",command=lambda:btnclick(2))
input_botton2.grid(row=4,column=1)

input_botton3=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="3",command=lambda:btnclick(3))
input_botton3.grid(row=4,column=2)

input_bottonAdd=Button(Calculator,padx=3,pady=5,bd=3,fg='black',
    font=('black',17,'bold'),text="+",command=lambda:btnclick("+"))
input_bottonAdd.grid(row=4,column=3)
input_bottonAC=Button(Calculator,padx=3,pady=6, width=2,bd=3,fg='black',
    font=('black',15,'bold'),text="AC",command=btnclear)
input_bottonAC.grid(row=5,column=0)
input_bottonzero=Button(Calculator,padx=3,pady=4,bd=3,fg='black',
    font=('black',17,'bold'),text="0",command=lambda:btnclick(0))
input_bottonzero.grid(row=5,column=1)
input_bottondot=Button(Calculator,padx=7,pady=4.3,bd=3,fg='black',
    font=('black',17,'bold'),text=".",command=lambda:btnclick('.'))
input_bottondot.grid(row=5,column=2)
input_bottonequals=Button(Calculator,padx=3,pady=6.6,bd=3,fg='black',
    font=('black',16,'bold'),text="=",command=btnEquals)
input_bottonequals.grid(row=5,column=3)
Calculator.mainloop()
