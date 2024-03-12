from tkinter import Tk,Frame,Button ,Label, StringVar

# # step1: Getting the default screen of the calculator

# # cal_screen = Tk()​
# # cal_screen.mainloop()​
# # Step2 : Giving the resolution of the calculator screen
# # cal_screen = Tk()​
# # cal_screen.geometry("500x500+450+100")
# ​
# # cal_screen.title("Calculator") # title of the screen.
# ​
# # cal_screen.resizable(0,0) # Disabling minimiza nd maximize button
# ​
# # cal_screen.mainloop()
# ​
# ​
# # Step3 : Diviging the screen into four frames.
# ​
# # cal_screen = Tk()
# ​
# ​
# # cal_screen.geometry("500x500+450+100")
# ​
# # cal_screen.title("Calculator") # title of the screen.
# ​
# # cal_screen.resizable(0,0) # Disabling minimiza nd maximize button
# ​
# ​
# # frame1 = Frame(cal_screen,bg="red")
# # frame1.pack(fill="both",expand=True)
# ​
# # frame2 = Frame(cal_screen,bg="blue")
# # frame2.pack(fill="both",expand=True)
# ​
# # frame3 = Frame(cal_screen,bg="green")
# # frame3.pack(fill="both",expand=True)
# ​
# # frame4 = Frame(cal_screen,bg="black")
# # frame4.pack(fill="both",expand=True)
# ​
# # cal_screen.mainloop()
# ​
# ​
# # Step4 : Adding the Buttons to the frames.
# ​
# # cal_screen = Tk()
# ​
# ​
# # cal_screen.geometry("500x500+450+100")
# ​
# # cal_screen.title("Calculator") # title of the screen.
# ​
# # cal_screen.resizable(0,0) # Disabling minimiza nd maximize button
# ​
# ​
# # frame1 = Frame(cal_screen,bg="red")
# # frame1.pack(fill="both",expand=True)
# ​
# # frame2 = Frame(cal_screen,bg="blue")
# # frame2.pack(fill="both",expand=True)
# ​
# # frame3 = Frame(cal_screen,bg="green")
# # frame3.pack(fill="both",expand=True)
# ​
# # frame4 = Frame(cal_screen,bg="black")
# # frame4.pack(fill="both",expand=True)
# ​
# ​
# ​
# # # Buttons
# ​
# # btn1 = Button(frame1,text="1",font=("arial",20,"bold"),border=0)
# # btn1.pack(side="left",fill="both",expand=True)
# ​
# # btn2 = Button(frame1,text="2",font=("arial",20,"bold"),border=0)
# # btn2.pack(side="left",fill="both",expand=True)
# ​
# # btn3 = Button(frame1,text="3",font=("arial",20,"bold"),border=0)
# # btn3.pack(side="left",fill="both",expand=True)
# ​
# # btnplus = Button(frame1,text="+",font=("arial",20,"bold"),border=0)
# # btnplus.pack(side="left",fill="both",expand=True)
# ​
# ​
# # btn4 = Button(frame2,text="4",font=("arial",20,"bold"),border=0)
# # btn4.pack(side="left",fill="both",expand=True)
# ​
# # btn5 = Button(frame2,text="5",font=("arial",20,"bold"),border=0)
# # btn5.pack(side="left",fill="both",expand=True)
# ​
# # btn6 = Button(frame2,text="6",font=("arial",20,"bold"),border=0)
# # btn6.pack(side="left",fill="both",expand=True)
# ​
# # btnminus = Button(frame2,text="-",font=("arial",20,"bold"),border=0)
# # btnminus.pack(side="left",fill="both",expand=True)
# ​
# ​
# # btn7 = Button(frame3,text="7",font=("arial",20,"bold"),border=0)
# # btn7.pack(side="left",fill="both",expand=True)
# ​
# # btn8 = Button(frame3,text="8",font=("arial",20,"bold"),border=0)
# # btn8.pack(side="left",fill="both",expand=True)
# ​
# # btn9 = Button(frame3,text="9",font=("arial",20,"bold"),border=0)
# # btn9.pack(side="left",fill="both",expand=True)
# ​
# # btnmul = Button(frame3,text="*",font=("arial",20,"bold"),border=0)
# # btnmul.pack(side="left",fill="both",expand=True)
# ​
# ​
# # btnC = Button(frame4,text="C",font=("arial",20,"bold"),border=0)
# # btnC.pack(side="left",fill="both",expand=True)
# ​
# # btn0 = Button(frame4,text="0",font=("arial",20,"bold"),border=0)
# # btn0.pack(side="left",fill="both",expand=True)
# ​
# # btnequal = Button(frame4,text="=",font=("arial",20,"bold"),border=0)
# # btnequal.pack(side="left",fill="both",expand=True)
# ​
# # btndiv = Button(frame4,text="/",font=("arial",20,"bold"),border=0)
# # btndiv.pack(side="left",fill="both",expand=True)
# ​
# ​
# # cal_screen.mainloop()
# ​
# ​
# # Step5: Defining the Label in the screen.
# ​
# # cal_screen = Tk()
# ​
# ​
# # cal_screen.geometry("500x500+450+100")
# ​
# # cal_screen.title("Calculator") # title of the screen.
# ​
# # cal_screen.resizable(0,0) # Disabling minimiza nd maximize button
# ​
# ​
# # sc_lbl = Label(cal_screen,text="Sample Label",font=("arial",20),bg="white",anchor="se")
# # sc_lbl.pack(fill="both",expand=True)
# ​
# # frame1 = Frame(cal_screen,bg="red")
# # frame1.pack(fill="both",expand=True)
# ​
# # frame2 = Frame(cal_screen,bg="blue")
# # frame2.pack(fill="both",expand=True)
# ​
# # frame3 = Frame(cal_screen,bg="green")
# # frame3.pack(fill="both",expand=True)
# ​
# # frame4 = Frame(cal_screen,bg="black")
# # frame4.pack(fill="both",expand=True)
# ​
# ​
# ​
# Buttons
# ​
# # btn1 = Button(frame1,text="1",font=("arial",20,"bold"),border=0)
# # btn1.pack(side="left",fill="both",expand=True)
# ​
# # btn2 = Button(frame1,text="2",font=("arial",20,"bold"),border=0)
# # btn2.pack(side="left",fill="both",expand=True)
# ​
# # btn3 = Button(frame1,text="3",font=("arial",20,"bold"),border=0)
# # btn3.pack(side="left",fill="both",expand=True)
# ​
# # btnplus = Button(frame1,text="+",font=("arial",20,"bold"),border=0)
# # btnplus.pack(side="left",fill="both",expand=True)
# ​
# ​
# # btn4 = Button(frame2,text="4",font=("arial",20,"bold"),border=0)
# # btn4.pack(side="left",fill="both",expand=True)
# ​
# # btn5 = Button(frame2,text="5",font=("arial",20,"bold"),border=0)
# # btn5.pack(side="left",fill="both",expand=True)
# ​
# # btn6 = Button(frame2,text="6",font=("arial",20,"bold"),border=0)
# # btn6.pack(side="left",fill="both",expand=True)
# ​
# # btnminus = Button(frame2,text="-",font=("arial",20,"bold"),border=0)
# # btnminus.pack(side="left",fill="both",expand=True)
# ​
# ​
# # btn7 = Button(frame3,text="7",font=("arial",20,"bold"),border=0)
# # btn7.pack(side="left",fill="both",expand=True)
# ​
# # btn8 = Button(frame3,text="8",font=("arial",20,"bold"),border=0)
# # btn8.pack(side="left",fill="both",expand=True)
# ​
# # btn9 = Button(frame3,text="9",font=("arial",20,"bold"),border=0)
# # btn9.pack(side="left",fill="both",expand=True)
# ​
# # btnmul = Button(frame3,text="*",font=("arial",20,"bold"),border=0)
# # btnmul.pack(side="left",fill="both",expand=True)
# ​
# ​
# # btnC = Button(frame4,text="C",font=("arial",20,"bold"),border=0)
# # btnC.pack(side="left",fill="both",expand=True)
# ​
# # btn0 = Button(frame4,text="0",font=("arial",20,"bold"),border=0)
# # btn0.pack(side="left",fill="both",expand=True)
# ​
# # btnequal = Button(frame4,text="=",font=("arial",20,"bold"),border=0)
# # btnequal.pack(side="left",fill="both",expand=True)
# ​
# # btndiv = Button(frame4,text="/",font=("arial",20,"bold"),border=0)
# # btndiv.pack(side="left",fill="both",expand=True)
# ​
# ​
# # cal_screen.mainloop()
# ​
# ​
# Setp6 : Defining the functions for the buttons.

cal_screen = Tk()

cal_screen.geometry("500x500+450+100")

cal_screen.title("Calculator") # title of the screen.

cal_screen.resizable(0,0) # Disabling minimiza nd maximize button

data = StringVar()

val = ""

def btn1_click():
    global val
    val = val+'1'
    data.set(val)

def btn2_click():
    global val
    val = val+'2'
    data.set(val)

def btn3_click():
    global val
    val = val+'3'
    data.set(val)
def btnplus_click():
    global val
    val = val+'+'
    data.set(val)

def btn4_click():
    global val
    val = val+'4'
    data.set(val)

def btn5_click():
    global val
    val = val+'5'
    data.set(val)

def btn6_click():
    global val
    val = val+'6'
    data.set(val)

def btnminus_click():
    global val
    val = val+'-'
    data.set(val)

def btn7_click():
    global val
    val = val+'7'
    data.set(val)

def btn8_click():
    global val
    val = val+'8'
    data.set(val)

def btn9_click():
    global val
    val = val+'9'
    data.set(val)

def btnmul_click():
    global val
    val = val+'*'
    data.set(val)

def btnC_click():
    global val
    val = ''
    data.set(val)

def btn0_click():
    global val
    val = val+'0'
    data.set(val)

def btnequal_click():
    global val
    val = str(eval(val))
    data.set(val)

def btndiv_click():
    global val
    val = val+'/'
    data.set(val)

sc_lbl = Label(cal_screen,text="Sample Label",font=("arial",20),bg="white",anchor="se",textvariable=data)
sc_lbl.pack(fill="both",expand=True)

frame1 = Frame(cal_screen,bg="red")
frame1.pack(fill="both",expand=True)

frame2 = Frame(cal_screen,bg="blue")
frame2.pack(fill="both",expand=True)

frame3 = Frame(cal_screen,bg="green")
frame3.pack(fill="both",expand=True)

frame4 = Frame(cal_screen,bg="black")
frame4.pack(fill="both",expand=True)

# Buttons

btn1 = Button(frame1,text="1",font=("arial",20,"bold"),border=0,command=btn1_click)
btn1.pack(side="left",fill="both",expand=True)

btn2 = Button(frame1,text="2",font=("arial",20,"bold"),border=0,command=btn2_click)
btn2.pack(side="left",fill="both",expand=True)

btn3 = Button(frame1,text="3",font=("arial",20,"bold"),border=0,command=btn3_click)
btn3.pack(side="left",fill="both",expand=True)

btnplus = Button(frame1,text="+",font=("arial",20,"bold"),border=0,command=btnplus_click)
btnplus.pack(side="left",fill="both",expand=True)

btn4 = Button(frame2,text="4",font=("arial",20,"bold"),border=0,command=btn4_click)
btn4.pack(side="left",fill="both",expand=True)

btn5 = Button(frame2,text="5",font=("arial",20,"bold"),border=0,command=btn5_click)
btn5.pack(side="left",fill="both",expand=True)

btn6 = Button(frame2,text="6",font=("arial",20,"bold"),border=0,command=btn6_click)
btn6.pack(side="left",fill="both",expand=True)

btnminus = Button(frame2,text="-",font=("arial",20,"bold"),border=0,command=btnminus_click)
btnminus.pack(side="left",fill="both",expand=True)

btn7 = Button(frame3,text="7",font=("arial",20,"bold"),border=0,command=btn7_click)
btn7.pack(side="left",fill="both",expand=True)

btn8 = Button(frame3,text="8",font=("arial",20,"bold"),border=0,command=btn8_click)
btn8.pack(side="left",fill="both",expand=True)

btn9 = Button(frame3,text="9",font=("arial",20,"bold"),border=0,command=btn9_click)
btn9.pack(side="left",fill="both",expand=True)

btnmul = Button(frame3,text="*",font=("arial",20,"bold"),border=0,command=btnmul_click)
btnmul.pack(side="left",fill="both",expand=True)
btnC = Button(frame4,text="C",font=("arial",20,"bold"),border=0,command=btnC_click)
btnC.pack(side="left",fill="both",expand=True)
btn0 = Button(frame4,text="0",font=("arial",20,"bold"),border=0,command=btn0_click)
btn0.pack(side="left",fill="both",expand=True)
btnequal = Button(frame4,text="=",font=("arial",20,"bold"),border=0,command=btnequal_click)
btnequal.pack(side="left",fill="both",expand=True)

btndiv = Button(frame4,text="/",font=("arial",20,"bold"),border=0,command=btndiv_click)
btndiv.pack(side="left",fill="both",expand=True)

cal_screen.mainloop()