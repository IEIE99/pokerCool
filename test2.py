import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", command = self.calculate)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = int(self.entry.get())
            result = "%s*2=%s" % (i, i*2)
        except ValueError:
            result = "Please enter digits only"

        # set the output widget to have our result
        self.output.configure(text=result)

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()



"""
"""
#Creating a GUI for entering name
def xyz():
    global a
    print (a.get()) 
from tkinter import *
root=Tk()  #It is just a holder
Label(root,text="ENter your name").grid(row=0,column=0) #Creating label
a=Entry(root)           #creating entry box
a.grid(row=7,column=8)
Button(root,text="OK",command=xyz).grid(row=1,column=1)
root.mainloop()           #important for closing th root=Tk()
"""
"""
import tkinter as tk
class Callback:
     def __init__(self, color):
         self.color = color
     def changeColor(self): 
         print('turn', self.color)
c1 = Callback('blue')
c2 = Callback('yellow')
B1 = tk.Button(command=c1.changeColor) 
B2 = tk.Button(command=c2.changeColor) 
B1.pack()
B2.pack()
