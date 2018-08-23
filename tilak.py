from tkinter import *
import tkinter



root=Tk()
root.title("FIM GUI")

topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root) 
bottomframe.pack(side='bottom')


#labels
data1=StringVar()
label_1=Label(topframe, text="input")
label_1.grid(row=0)
Entry=Entry(topframe,textvariable=data1)

Entry.grid(row=0,column=1)

#buttons
button1=tkinter.Button(topframe, text="start", command="")
button1.grid(row=1,column=0)
button2=tkinter.Button(topframe, text="stop ", command="")
button2.grid(row=1,column=1)

root.mainloop()