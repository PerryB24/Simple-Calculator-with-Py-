from tkinter import *
 
root = Tk()
root.title("Simple calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


'''
#Creating a label widget
myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Perry Butler")

#Shoving it onto the screen
myLabel.grid(row= 0, column=0)
myLabel2.grid(row=1, column=0)
'''


def button_click(num):
    #e.delete(0, END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))

def button_clear():
    e.delete(0,END)

def button_add():
    global symbol
    symbol = "+"
    number1 = e.get()
    global f_num
    f_num = float(number1)
    e.delete(0,END)
def button_multiplication():
    global symbol 
    symbol = "*"
    number1 = e.get()
    global f_num
    f_num = float(number1)
    e.delete(0,END)
def button_division():
    global symbol 
    symbol = "/"
    number1 = e.get()
    global f_num
    f_num = float(number1)
    e.delete(0,END)

def button_subtraction():
    global symbol
    symbol = "-"
    number1 = e.get()
    global f_num
    f_num = float(number1)
    e.delete(0,END)

def button_equalto():
    number2 = e.get()
    e.delete(0,END)
    if(symbol=="+"):
        e.insert(0, f_num + int(number2))
    elif(symbol=="-"):
        e.insert(0, f_num - int(number2))
    elif(symbol=="/"):
        e.insert(0, f_num / int(number2))
    elif(symbol=="*"):
        e.insert(0, f_num * int(number2))

#Define your buttons
button_1 = Button(root, text="1", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", activebackground='light blue',padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text="+", activebackground='light blue',padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", activebackground='light blue',padx=40, pady=20, command=button_subtraction)
button_divide = Button(root, text="/", activebackground='light blue',padx=40, pady=20, command=button_division)
button_multiply = Button(root, text="X", activebackground='light blue',padx=40, pady=20, command=button_multiplication)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equalto)
button_Clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)


# Put buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_Clear.grid(row=4,column=1, columnspan=2)
button_addition.grid(row=5,column=0)

button_equal.grid(row=5,column=1, columnspan=2)
button_subtract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)

button_multiply.grid(row=6,column=2)


'''myButton.pack()'''

root.mainloop()