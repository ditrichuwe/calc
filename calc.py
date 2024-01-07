import tkinter

def plus():
    num1=int(textnum3.get())
    num2=int(textnum2.get())
    textnum1.delete(0,"end")
    textnum1.insert(0,num1+num2)

def minus():
    num1=int(textnum3.get())
    num2=int(textnum2.get())
    textnum1.delete(0,"end")
    textnum1.insert(0,num1-num2)

def division():
    num1=int(textnum3.get())
    num2=int(textnum2.get())
    textnum1.delete(0,"end")
    textnum1.insert(0,num1/num2)

def multiplication():
    num1=int(textnum3.get())
    num2=int(textnum2.get())
    textnum1.delete(0,"end")
    textnum1.insert(0,num1*num2)

window=tkinter.Tk()
window.title("NikCalculator")
window.geometry("1000x1000")

#plusbuton
buttonad=tkinter.Button(window,text="+",command=plus)
buttonad.place(x=230,y=150)
buttonad["bg"]="#34ebe5"

#subtractionsbutton
buttonsub=tkinter.Button(window,text="-",command=minus)
buttonsub.place(x=230,y=100)

#divisionsbutton
buttondiv=tkinter.Button(window,text="/",command=division)
buttondiv.place(x=230,y=50)

#multiplicationsbutton
buttonmulti=tkinter.Button(window,text="*",command=multiplication)
buttonmulti.place(x=230,y=200)

textnum1=tkinter.Entry(window,width=25)
textnum1.place(x=80,y=90)

textnum2=tkinter.Entry(window,width=25)
textnum2.place(x=80,y=45)

textnum3=tkinter.Entry(window,width=25)
textnum3.place(x=80,y=0)



















































window.mainloop()
