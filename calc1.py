import tkinter

def plus():
     global first_number,sign
     first_number=int(textnum1.get())
     textnum1.delete(0,"end")
     sign="+"

def minus():
     global first_number,sign
     first_number=int(textnum1.get())
     textnum1.delete(0,"end")
     sign="-"
def division():
     global first_number,sign
     first_number=int(textnum1.get())
     textnum1.delete(0,"end")
     sign="/"

def multiplication():
     global first_number,sign
     first_number=int(textnum1.get())
     textnum1.delete(0,"end")
     sign="*"

def equal():
     global second_number,first_number,sign
     second_number=int(textnum1.get())
     textnum1.delete(0,"end")
     if sign=="+":
          textnum1.insert(0,round(first_number+second_number,3))
     elif sign=="-":
          textnum1.insert(0,round(first_number-second_number,3))
     elif sign=="/":
          textnum1.insert(0,round(first_number/second_number,3))
     elif sign=="*":
          textnum1.insert(0,round(first_number*second_number,3))



def insertsign(sign):
    lenght=len(textnum1.get())
    textnum1.insert(lenght,sign)

window=tkinter.Tk()
window.title("NikCalculator")
window.geometry("300x300")


first_number=0
second_number=0

sign=""

#plusbuton
buttonad=tkinter.Button(window,text="+",command=plus,width=5)
buttonad.place(x=140,y=150)
buttonad["bg"]="#34ebe5"

#subtractionsbutton
buttonsub=tkinter.Button(window,text="-",command=minus)
buttonsub.place(x=140,y=130)
buttonad["bg"]="#34ebe5"

#divisionsbutton
buttondiv=tkinter.Button(window,text="/",command=division)
buttondiv.place(x=140,y=110)
buttonad["bg"]="#34ebe5"

#multiplicationsbutton
buttonmulti=tkinter.Button(window,text="*",command=multiplication)
buttonmulti.place(x=110,y=180)
buttonad["bg"]="#34ebe5"

#commabutton
buttoncomma=tkinter.Button(window,text=",")
buttoncomma.place(x=120,y=180)
buttonad["bg"]="#34ebe5"

#answerbutton
buttonanswer=tkinter.Button(window,text="=",command=equal)
buttonanswer.place(x=140,y=180)
buttonad["bg"]="#34ebe5"



#1button
button1=tkinter.Button(window,text="1",command=lambda sign="1":insertsign(sign))
button1.place(x=100,y=150)

#2button
button2=tkinter.Button(window,text="2",command=lambda sign="2":insertsign(sign))
button2.place(x=110,y=150)

#3button
button3=tkinter.Button(window,text="3",command=lambda sign="3":insertsign(sign))
button3.place(x=120,y=150)

#4button
button4=tkinter.Button(window,text="4")
button4.place(x=100,y=130)

#5button
button5=tkinter.Button(window,text="5")
button5.place(x=110,y=130)

#6button
button6=tkinter.Button(window,text="6")
button6.place(x=120,y=130)

#7button
button7=tkinter.Button(window,text="7")
button7.place(x=100,y=110)

#8button
button8=tkinter.Button(window,text="8")
button8.place(x=110,y=110)

#9button
button9=tkinter.Button(window,text="9")
button9.place(x=120,y=110)



textnum1=tkinter.Entry(window,width=25)
textnum1.place(x=80,y=90)






















































window.mainloop()
