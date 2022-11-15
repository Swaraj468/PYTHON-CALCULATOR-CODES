root.mainloop()
def exit():
    x = tkinter.messagebox.askquestion("Exit","Do you really want to exit",icon="warning")
    if x == "yes":
        root.destroy()

Button(root,text="Exit",fg="white",bg="black",font="arial 18 bold",command=exit).place(y=500)