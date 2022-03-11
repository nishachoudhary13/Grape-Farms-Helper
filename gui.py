import sys
import os
import tkinter
from tkinter import *
from PIL import ImageTk,Image

top=Tk()

def onClickWeed():
    os.system('python try.py')

def onClickHarvest():
    os.system('python harvest.py')

def onClickDisease():
    os.system('python table.py')
    
top.geometry("1000x1000")
top.title("Automated Guided Vehicle")

label = Label(top, text="Automated Guided Vehicle", relief = "solid", width = 20, font=("arial") )
label.place(x=90,y=53)

W=tkinter.Button(top,text="Weed Detection",width=18,bg='green',fg='white',command= onClickWeed)
W.place(x=80,y=130)
W.pack()
H=tkinter.Button(top,text="Fruit Harvesting",width=18,bg='green',fg='white',command= onClickHarvest)
H.place(x=80,y=179)
H.pack()
D=tkinter.Button(top,text="Disease Detection",width=18,bg='green',fg='white',command= onClickDisease)
D.place(x=80,y=228)
D.pack()

top.mainloop()

