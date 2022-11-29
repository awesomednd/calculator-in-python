import tkinter as tk
from decimal import Decimal
from math import sqrt
from math import pow
from decimal import *

calc = tk.Tk()

frame1 = tk.Frame(master=calc, width=600, height=400, )
frame1.pack()

display_text2 = tk.Variable()
m1 = tk.Variable()
s3 = tk.DoubleVar()
o = tk.Variable()
display_text = tk.Variable()
FUNCT = tk.Variable()

display_answer2 = tk.Label(master=frame1, textvariable=display_text2, width=45, height=2, wraplength=300)
display_answer2.place(x=1, y=10)


display_answer = tk.Label(master=frame1, textvariable=display_text, width=45, height=2, wraplength=300)
display_answer.place(x=1, y=60)


def point():
    s = display_text.get()
    s += '.'
    display_text.set(s)


def num_one():
    s = display_text.get()
    s += '1'
    display_text.set(s)


def num_two():
    s = display_text.get()
    s += '2'
    display_text.set(s)


def num_three():
    s = display_text.get()
    s += '3'
    display_text.set(s)


def num_four():
    s = display_text.get()
    s += '4'
    display_text.set(s)


def num_five():
    s = display_text.get()
    s += '5'
    display_text.set(s)


def num_six():
    s = display_text.get()
    s += '6'
    display_text.set(s)


def num_seven():
    s = display_text.get()
    s += '7'
    display_text.set(s)


def num_eight():
    s = display_text.get()
    s += '8'
    display_text.set(s)


def num_nine():
    s = display_text.get()
    s += '9'
    display_text.set(s)


def num_zero():
    s = display_text.get()
    s += '0'
    display_text.set(s)


def ac():
    s = ''
    s2 = ''
    s3.set(s2)
    o2 = ""
    o.set(o2)
    display_text2.set(s)
    display_text.set(s)
    FUNCT.set(s)


def add2():
    s2 = display_text.get()
    s3.set(s2)
    s = ''
    o2 = 'addition'
    o.set(o2)
    display_text.set(s)
    s7 = '+'
    FUNCT.set(s7)
    display_text2.set(s2)


def sub():
    s2 = display_text.get()
    s3.set(s2)
    s = ''
    o2 = 'subtraction'
    o.set(o2)
    display_text.set(s)
    s7 = '-'
    FUNCT.set(s7)
    display_text2.set(s2)


def times():
    s2 = display_text.get()
    s3.set(s2)
    s = ''
    o2 = 'times'
    o.set(o2)
    display_text.set(s)
    s7 = 'X'
    FUNCT.set(s7)
    display_text2.set(s2)


def div():
    s2 = display_text.get()
    s3.set(s2)
    s = ''
    o2 = 'divide'
    o.set(o2)
    display_text.set(s)
    s7 = '÷'
    FUNCT.set(s7)
    display_text2.set(s2)


def sr():
    s2 = display_text.get()
    a = sqrt(Decimal(s2))
    display_text.set(a)
    s7 = '√'
    FUNCT.set(s7)


def sr3():
    s2 = display_text.get()
    s5 = abs(int(s2))
    a = pow(s5, 1/3)
    display_text.set(a)
    s7 = '3√'
    FUNCT.set(s7)


def pwr():
    s6 = display_text.get()
    s7 = '^'
    o2 = 'power'
    o.set(o2)
    s = ''
    display_text.set(s)
    s3.set(s6)
    FUNCT.set(s7)
    display_text2.set(s6)


def neg():
    s2 = display_text.get()
    s = -abs(Decimal(s2))
    display_text.set(s)


def pi():
    s2 = display_text.get()
    s = s2 + '3.1415926535'
    display_text.set(s)


def stf():
    s6 = display_text.get()
    o2 = 'stf'
    o.set(o2)
    s7 = ''
    display_text.set(s7)
    FUNCT.set(o2)
    display_text2.set(s6)
    s3.set(s6)


def equal():
    o2 = o.get()
    if o2 == "addition":
        s2 = s3.get()
        s4 = display_text.get()
        a = add(Decimal(s2), Decimal(s4))
        print(a)
        display_text.set(a)
        s = ''
        display_text2.set(s)
    elif o2 == "subtraction":
        s2 = s3.get()
        s4 = display_text.get()
        a = sub2(Decimal(s2), Decimal(s4))
        print(a)
        display_text.set(a)
        s = ''
        display_text2.set(s)
    elif o2 == "times":
        s2 = s3.get()
        s4 = display_text.get()
        a = times2(Decimal(s2), Decimal(s4))
        print(a)
        display_text.set(a)
        s = ''
        display_text2.set(s)
    elif o2 == "divide":
        s2 = s3.get()
        s4 = display_text.get()
        a = div2(Decimal(s2), Decimal(s4))
        print(a)
        display_text.set(a)
        s = ''
        display_text2.set(s)
    elif o2 == "power":
        s2 = s3.get()
        s4 = display_text.get()
        a = pow(Decimal(s2), Decimal(s4))
        display_text.set(a)
        s = ''
        display_text2.set(s)
    elif o2 == "stf":
        s2 = s3.get()
        s4 = display_text.get()
        r = s4
        a4 = int(10) ** int(r)
        a = times2(Decimal(s2), Decimal(a4))
        display_text.set(a)
        s = '0'
        display_text2.set(s)
    else:
        a = "Please use an operation and try again and hit the AC button to clear"
        display_text.set(a)


def add(c, b):
    return c + b


def sub2(c, b):
    return c - b


def div2(c, b):
    return c / b


def times2(c, b):
    return c * b


def mp():
    m2 = display_text.get()
    m1.set(m2)


def mm():
    m2 = m1.get()
    display_text.set(m2)
    

def power2(c, b):
    return c ** b


def del2():
    s = ''
    display_text.set(s)


label1 = tk.Button(master=frame1, text="1", width=10, height=5, command=num_one)
label1.place(x=0, y=100)

label2 = tk.Button(master=frame1, text="2", width=10, height=5, command=num_two)
label2.place(x=100, y=100)

label3 = tk.Button(master=frame1, text="3", width=10, height=5, command=num_three)
label3.place(x=200, y=100)

label4 = tk.Button(master=frame1, text="4", width=10, height=5, command=num_four)
label4.place(x=0, y=200)

label5 = tk.Button(master=frame1, text="5", width=10, height=5, command=num_five)
label5.place(x=100, y=200)

label6 = tk.Button(master=frame1, text="6", width=10, height=5, command=num_six)
label6.place(x=200, y=200)

label7 = tk.Button(master=frame1, text="7", width=10, height=5, command=num_seven)
label7.place(x=0, y=300)

label8 = tk.Button(master=frame1, text="8", width=10, height=5, command=num_eight)
label8.place(x=100, y=300)

label9 = tk.Button(master=frame1, text="9", width=10, height=5, command=num_nine)
label9.place(x=200, y=300)

label0 = tk.Button(master=frame1, text="0", width=10, height=5, command=num_zero)
label0.place(x=300, y=100)

labelAC = tk.Button(master=frame1, text="AC", width=10, height=5, command=ac)
labelAC.place(x=400, y=100)

labelADD = tk.Button(master=frame1, text="+", width=10, height=5, command=add2)
labelADD.place(x=300, y=200)

labelSUB = tk.Button(master=frame1, text="-", width=10, height=5, command=sub)
labelSUB.place(x=400, y=200)

labelX = tk.Button(master=frame1, text="X", width=10, height=5, command=times)
labelX.place(x=300, y=300)

labelDIV = tk.Button(master=frame1, text="÷", width=10, height=5, command=div)
labelDIV.place(x=400, y=300)

labelEQUAL = tk.Button(master=frame1, text="=", width=2, height=2, command=equal)
labelEQUAL.place(x=450, y=10)

labelPOINT = tk.Button(master=frame1, text=".", width=2, height=1, command=point)
labelPOINT.place(x=450, y=60)

labelSR = tk.Button(master=frame1, text="√", width=10, height=5, command=sr)
labelSR.place(x=500, y=100)

labelSR3 = tk.Button(master=frame1, text="3√", width=10, height=5, command=sr3)
labelSR3.place(x=500, y=200)

labelPWR = tk.Button(master=frame1, text="^", width=10, height=5, command=pwr)
labelPWR.place(x=500, y=300)

labelFUNC = tk.Label(master=frame1, textvariable=FUNCT, width=1, height=1, font=16)
labelFUNC.place(x=550, y=30)

labelNEG = tk.Button(master=frame1, text="(-)", width=2, height=2, command=neg)
labelNEG.place(x=500, y=10)


labelPI = tk.Button(master=frame1, text="π", width=2, height=1, command=pi)
labelPI.place(x=500, y=60)

labelSF = tk.Button(master=frame1, text="X10^x", width=2, height=1, command=stf)
labelSF.place(x=550, y=60)

LabelMP = tk.Button(master=frame1, text="M+", width=2, height=2, command=mp)
LabelMP.place(x=400, y=10)

labelMM = tk.Button(master=frame1, text="M-", width=2, height=1, command=mm)
labelMM.place(x=400, y=60)

labelDEL = tk.Button(master=frame1, text="DEL", width=2, height=1, command=del2)
labelDEL.place(x=350, y=60)

calc.mainloop()
