import tkinter as tk
#from tkinter import messagebox
import os
import csv
import time

#Csv File Reader
filepath = 'test.csv'
File = open(filepath)
Reader = csv.reader(File)
data = list(Reader)
print(data[3][-1])

#Basic Tkinter GUI start up
root = tk.Tk()
root.title('Stresson')
root.geometry('400x400')
root.resizable(False, False)
bg1 = tk.PhotoImage(file="tech.png")

label0 = tk.Label(image=bg1)
label0.place(x=0, y=0)


#When Button for record pressed, opens new frame
def record():
    #Insert Code Here
    #os.system('python test.py') #Repl.it Test
    os.system('python collectData.py') #Stresson Record Actual
    
    #After 5 seconds of recording measurements, values will be shown
    time.sleep(5)
    labelGsr.config(text=data[-1][0])
    labelTemp.config(text=data[-1][1])
    labelHR.config(text=data[-1][2])
    labelSp02.config(text=data[-1][3])
    #messagebox.showinfo("Information","Showing Results")
    
#When Button for graph pressed, opens new frame
def graph():
    #Insert Code Here
    os.system('python plotData.py')


#Work on gettting Date appendid to end of Csv file
def enterDate():
    #Date = entry1.get()
    #print(Date)
    tempData=[entry1.get()]
    data.append(tempData)

# Position Frames
frame1 = tk.LabelFrame(root, text="")  #Middle Frame
frame2 = tk.LabelFrame(root, text="")  #Top Frame
frame3 = tk.LabelFrame(root, text="")  #Bottom Frame
frame4 = tk.LabelFrame(root, text="")  #2nd Middle Frame

frame2.pack(padx=10, pady=10)
frame1.pack(padx=10, pady=10)
frame4.pack(padx=10, pady=10)
frame3.pack(padx=10, pady=10)

#Lables
dateLabel = tk.Label(frame2, text="Input Date:")
dateLabel.pack(side="left")

dateEnter = tk.Button(frame2, text="Enter", command=enterDate)
dateEnter.pack(side="right")

#Entries
entry1 = tk.Entry(frame2, width=5)
entry1.pack(side="left")

#Labels contined for record action
labelGsrTxt = tk.Label(frame4, text="GSR:", width=5)
labelTempTxt = tk.Label(frame4, text="Temp:", width=5)
labelHRTxt = tk.Label(frame4, text="HR:", width=5)
labelSp02Txt = tk.Label(frame4, text="Sp02:", width=5)

labelGsr = tk.Label(frame4, text="", width=5)
labelTemp = tk.Label(frame4, text="", width=5)
labelHR = tk.Label(frame4, text="", width=5)
labelSp02 = tk.Label(frame4, text="", width=5)

#Buttons
recordButton = tk.Button(frame1, text="Record", command=record)
GraphButton = tk.Button(frame3, text="Graph", command=graph)

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


root.mainloop()