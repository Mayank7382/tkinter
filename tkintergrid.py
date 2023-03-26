from tkinter import *

root = Tk()

#creating a Label Widget
myLabel1 = Label(root,text="Hello Mayank")
myLabel2 = Label(root,text="Hello Mayank gupta")
myLabel3 = Label(root,text="123")
#showing it onto screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)
myLabel1.grid(row=0,column=0)


root.mainloop()