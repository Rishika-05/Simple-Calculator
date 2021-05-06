from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=8, pady=2)


def add(number):
    global math
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number)) 
    

def clear():
    e.delete(0, END)
    
def sm():
    a=e.get()
    global math
    global an
    math = "addition"
    an = int(a)
    e.delete(0,END)
    
def ans():
    b=e.get()
    global math
    e.delete(0,END)
    if math=="addition":
     e.insert(0,an+int(b)) 
    elif math=="multiply":
     e.insert(0,an*int(b)) 
    elif math=="subtraction":
     e.insert(0,an-int(b))
    elif math=="divide":
     e.insert(0,an/int(b))
     
     math="equal"
    
def mul():
    a=e.get()
    global math
    global an
    math = "multiply"
    an = int(a)
    e.delete(0,END)

def sub():
    a=e.get()
    global math
    global an
    math = "subtraction"
    an = int(a)
    e.delete(0,END)

def div():
    a=e.get()
    global math
    global an
    math = "division"
    an = int(a)
    e.delete(0,END)
    

b1= Button(root,text="1", padx=40, pady=20, command=lambda: add(1))
b2= Button(root,text="2", padx=40, pady=20, command=lambda: add(2))
b3= Button(root,text="3", padx=40, pady=20, command=lambda: add(3))
b4= Button(root,text="4", padx=40, pady=20, command=lambda: add(4))
b5= Button(root,text="5", padx=40, pady=20, command=lambda: add(5))
b6= Button(root,text="6", padx=40, pady=20, command=lambda: add(6))
b7= Button(root,text="7", padx=40, pady=20, command=lambda: add(7))
b8= Button(root,text="8", padx=40, pady=20, command=lambda: add(8))
b9= Button(root,text="9", padx=40, pady=20, command=lambda: add(9))
b0= Button(root,text="0", padx=40, pady=20, command=lambda: add(0))
bc=Button(root,text="Clear",padx=79,pady=20, command=clear)
be=Button(root,text="=", padx=91, pady=20, command=ans)
ba=Button(root,text="+", padx=39, pady=20, command=sm)
bm=Button(root,text="*", padx=39, pady=20, command=mul)
bs=Button(root,text="-", padx=40, pady=20, command=sub)
bd=Button(root,text="/", padx=40, pady=20, command=div)

# put button screen 
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
bc.grid(row=4, column=1, columnspan=2)

ba.grid(row=5, column=0)
be.grid(row=5, column=1, columnspan=2)

bs.grid(row=6, column=0)
bm.grid(row=6, column=1)
bd.grid(row=6, column=2)

root.mainloop()
