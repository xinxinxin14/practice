from tkinter import *
import tkinter.messagebox as messagebox

messagebox.showinfo('Message','please enter your name')
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='hey',command = self.hello)
        self.alertButton.pack()


    def hello(self):
        name = self.nameInput.get()or'world'
        messagebox.showinfo('Message','hello,%s'% name)


app = Application()

app.master.title('hello')

app.mainloop
