# GUI Calculator

from tkinter import *

exp = ""

def press(num):
    global exp
    exp = exp + str(num)
    txt.set(exp)

def clr():
    global exp
    exp = ""
    txt.set("")
    
def eq2():
    try:
        global exp
        tot=str(eval(exp))
        txt.set(tot)
        exp = tot
    except:
        exp = ""
        txt.set("Error")

disp = Tk()
disp.title("Simple Calculator")
disp.configure(background = "grey")
txt = StringVar()
entry = Entry(disp, borderwidth=5, textvariable=txt)
entry.grid(row=0,column=0, columnspan=4, padx=10, pady=10)
entry.insert(0,"Enter Your Number")


b1 = Button(disp, text = "1",bg = '#FEF0E3', command = lambda : press("1"))
b1.grid(row=3,column=0,padx=10,pady=10)
b2 = Button(disp, text = "2",bg = '#FEF0E3', command = lambda : press("2"))
b2.grid(row=3,column=1,padx=10,pady=10)
b3 = Button(disp, text = "3",bg = '#FEF0E3', command = lambda : press("3"))
b3.grid(row=3,column=2,padx=10,pady=10)
b4 = Button(disp, text = "4",bg = '#FEF0E3', command = lambda : press("4"))
b4.grid(row=2,column=0,padx=10,pady=10)
b5 = Button(disp, text = "5",bg = '#FEF0E3', command = lambda : press("5"))
b5.grid(row=2,column=1,padx=10,pady=10)
b6 = Button(disp, text = "6",bg = '#FEF0E3', command = lambda : press("6"))
b6.grid(row=2,column=2,padx=10,pady=10)
b7 = Button(disp, text = "7",bg = '#FEF0E3', command = lambda : press("7"))
b7.grid(row=1,column=0,padx=10,pady=10)
b8 = Button(disp, text = "8",bg = '#FEF0E3', command = lambda : press("8"))
b8.grid(row=1,column=1,padx=10,pady=10)
b9 = Button(disp, text = "9",bg = '#FEF0E3', command = lambda : press("9"))
b9.grid(row=1,column=2,padx=10,pady=10)
b0 = Button(disp, text = "0",bg = '#FEF0E3', command = lambda : press("0"))
b0.grid(row=4,column=1,padx=10,pady=10)


add = Button(disp, text = "+",bg = '#FEF0E3', command = lambda : press("+"))
add.grid(row=1,column=3,padx=10,pady=10)
sub = Button(disp, text = "-",bg = '#FEF0E3', command = lambda : press("-"))
sub.grid(row=2,column=3,padx=10,pady=10)
mul = Button(disp, text = "*",bg = '#FEF0E3', command = lambda : press("*"))
mul.grid(row=3,column=3,padx=10,pady=10)
div = Button(disp, text = "/",bg = '#FEF0E3', command = lambda : press("/"))
div.grid(row=4,column=3,padx=10,pady=10)
equal = Button(disp, text = "=",bg = '#FEF0E3', command = eq2)
equal.grid(row=4,column=2,padx=10,pady=10)
clear = Button(disp, text = "CLR",bg = '#FEF0E3', command = clr)
clear.grid(row=4,column=0,padx=10,pady=10)


disp.mainloop()
