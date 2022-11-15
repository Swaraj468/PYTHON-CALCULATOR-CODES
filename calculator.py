from tkinter import *
import math
import tkinter.messagebox


def click(value):
    print(value)
    answer = ''
    ex = entryField.get()

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]
            print("hello")
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == "CE":
            entryField.delete(0, "end")

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'Cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'Sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # 7**5
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == 'rad':
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log10':
            answer = math.log10(eval(ex))

        elif value == 'X!':
            answer = math.factorial(int(ex))

        elif value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except Exception as e:
        entryField.delete(0, END)
        entryField.insert(0, "invalid syntax")


root = Tk()
root.title("Calculator")
root.geometry("690x550")
root.config(bg="grey")

# logoimage = PhotoImage(file="cal1.png",height=100,width=100)
# logolabel = Label(root,image=logoimage)
# logolabel.grid(row =0,column=0)

entryField = Entry(root, font="arial 45 bold", bg="white",
                   fg="black", bd=10, relief=SUNKEN)
entryField.grid(row=0, column=0, columnspan=8)

button_text_list = ["C", "CE", "√", "+", "π", "Cosθ", "Sinθ", "tanθ",
                    "1", "2", "3", "-", "2π", "cosh", "sinh", "tanh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log10", "(", ")", "X!"]

# x\u02b8  ->cube root
# x\u02b8  ->x^y
# chr(247) -> division

row_value = 1
column_value = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg="black",
                    font="aria 18 bold", activebackground="honeydew3", fg="white",
                    command=lambda button=i: click(button))
    button.grid(row=row_value, column=column_value, pady=1, padx=1)
    column_value += 1
    if column_value > 7:
        row_value += 1
        column_value = 0

root.mainloop()
def exit():
    x = tkinter.messagebox.askquestion("Exit","Do you really want to exit",icon="warning")
    if x == "yes":
        root.destroy()

Button(root,text="Exit",fg="white",bg="black",font="arial 18 bold",command=exit).place(y=500)