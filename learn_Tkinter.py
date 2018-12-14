from tkinter import *
root = Tk()

li = ['hello','hi','are you ok?']
movie = ['hey','yoah',' i am fine']

list1 = Listbox(root)
list2 = Listbox(root)
for i in li:
    list1.insert(0,i)

for i in movie:
    list2.insert(0,i)

list1.pack()
list2.pack()
root.mainloop()
