import tkinter as tk
from tkinter import ttk
import os
import csv
#from tkinter import messagebox


#Basic Tkinter GUI start up
root = tk.Tk()
root.title('Stresson')
root.geometry('800x400')
root.resizable(False, False)
bg1 = tk.PhotoImage(file="StressonLogo.png")
bg2 = tk.PhotoImage(file="StressRanges2.png")
bg3 = tk.PhotoImage(file="Red.png")
bg4 = tk.PhotoImage(file="Tips.png")


label0 = tk.Label(image=bg1)
label0.place(x=0, y=0)

label1 = tk.Label(image=bg2)
label1.place(x=400, y=0)

label2 = tk.Label(image=bg3)
label2.place(x=400, y=184)

#When Button for record pressed, opens new frame
def record():
  x=1
  rows=[]
    
  with open("test.csv", 'r') as f:
    csvreader = csv.reader(f)
    rows = list(csvreader)
    print(rows[x])

  labelGsr.config(text=rows[-1][3])
  labelTemp.config(text=rows[-1][2])
  labelHR.config(text=rows[-1][4])
  labelSp02.config(text=rows[-1][1])
  labelHRV.config(text=rows[-1][5])



#When Button for graph pressed, opens new frame
def graph():
  #Insert Code Here
  os.system('python plotData.py')
    
  rows=[]
    
  with open("stressLevel.csv", 'r') as f:
    csvreader = csv.reader(f)
    rows = list(csvreader)
    print(rows[1])

  HRLabel.config(text=rows[-1][3])
  HRVLabel.config(text=rows[-1][2])
  Sp02Label.config(text=rows[-1][4])
  TempLabel.config(text=rows[-1][1])
  GSRLabel.config(text=rows[-1][5])

def tips():
  tipsWindow = tk.Toplevel(root)
  tipsWindow.title("Stresson")
  tipsWindow.resizable(False, False)
  tipsWindow.geometry("400x285")
  label3 = tk.Label(tipsWindow, image=bg4)
  label3.pack()

#Regular Frames
frame1 = tk.LabelFrame(root, text="")  #Middle Frame
frame3 = tk.LabelFrame(root, text="")  #2nd Middle Frame
frame4 = tk.LabelFrame(root, text="")  #Bottom Frame
frame5 = tk.LabelFrame(root, text="")  #Last Frame

frame1.place(x=155, y=20)
frame3.place(x=157, y=70)
frame4.place(x=50, y=340)
frame5.place(x=100, y=300)


#Labels contined for record action
labelGsrTxt = tk.Label(frame4, text="GSR:",bg='white' , width=5)
labelTempTxt = tk.Label(frame4, text="Temp:",bg='white' , width=5)
labelHRTxt = tk.Label(frame5, text="HR:",bg='white' , width=5)
labelSp02Txt = tk.Label(frame4, text="Sp02:",bg='white' , width=5)
labelHRVTxt = tk.Label(frame5, text="HRV:",bg='white' , width=5)

labelGsr = tk.Label(frame4, text="", bg='white' ,width=5)
labelTemp = tk.Label(frame4, text="",bg='white' , width=5)
labelHR = tk.Label(frame5, text="",bg='white' , width=5)
labelSp02 = tk.Label(frame4, text="",bg='white' , width=5)
labelHRV = tk.Label(frame5, text="",bg='white' , width=5)

#Buttons
recordButton = tk.Button(frame1, text="Record", bg='white' ,command=record)
GraphButton = tk.Button(frame3, text="Graph", bg='white' ,command=graph)

#Record and Grapgh
recordButton.pack()
GraphButton.pack()

#GSR, Temp, HR etc from csv showings
labelGsrTxt.pack(side='left')
labelGsr.pack(side='left')

labelTempTxt.pack(side='left')
labelTemp.pack(side='left')

labelHRTxt.pack(side='left')
labelHR.pack(side='left')

labelSp02Txt.pack(side='left')
labelSp02.pack(side='left')

labelHRVTxt.pack(side='left')
labelHRV.pack(side='left')

separator = ttk.Separator(root, orient='vertical')
separator.place(relx=0.50, rely=0, relwidth=0, relheight=1)

stressLabel = tk.Label(root, bg = 'white', text="Stress Results", relief="solid")
stressLabel.place(x=550,y=190)

HR = tk.Label(root, bg = 'white', text="HR", width=5, relief="groove")
HRV = tk.Label(root, bg = 'white', text="HRV", width=5, relief="groove")
Sp02 = tk.Label(root, bg = 'white', text="Sp02", width=5, relief="groove")
Temp =tk.Label(root, bg = 'white', text="Temp", width=5, relief="groove")
GSR =tk.Label(root, bg = 'white', text="GSR", width=5, relief="groove")

HR.place(x=410,y=220)
HRV.place(x=410,y=245)
Sp02.place(x=410,y=270)
Temp.place(x=410,y=295)
GSR.place(x=410,y=320)

HRLabel =  tk.Label(root, bg = 'white', text="", width=35)
HRVLabel = tk.Label(root, bg = 'white', text="", width=35)
Sp02Label = tk.Label(root, bg = 'white', text="", width=35)
TempLabel = tk.Label(root, bg = 'white', text="", width=35)
GSRLabel = tk.Label(root, bg = 'white', text="", width=35)

HRLabel.place(x=465,y=220)
HRVLabel.place(x=465,y=245)
Sp02Label.place(x=465,y=270)
TempLabel.place(x=465,y=295)
GSRLabel.place(x=465,y=320)


tipButton = tk.Button(root, text= 'Tips', bg='White', command = tips)
tipButton.place(x=575,y=350)

root.mainloop()
