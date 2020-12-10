import tkinter as tk
import tkinter.font as font

root = tk.Tk()

expression = ""



def clear():
    global expression
    expression = ""
    equation.set("0")


def back():
    global expression
    expression = expression[:-1]
    if expression == "":
        equation.set("0")
    else:
        equation.set(expression)


def Plusminus():
    global expression
    if expression.startswith('-'):
        expression = expression[1:]
        equation.set(expression)
    else:
        expression = "-" + expression
        equation.set(expression)


root.geometry("320x450")
root.minsize(320, 450)
root.maxsize(320, 450)
root.title("Calculator")
root.configure(bg="#131313")
myFont = font.Font(size=60)
myFont1 = font.Font(size=20)
myFont3 = font.Font(size=10)
myFont2 = font.Font(size=30)

if __name__ == '__main__':
    equation = tk.StringVar()
    pe = tk.StringVar()
    expression_field = tk.Entry(root, textvariable=equation, bg="#131313", fg="White", border=0)
    expression_field['font'] = myFont
    expression_field.pack()
    expression_field.place(x=5, y=30)
    equation.set('0')


    def equal(event=None):
        try:
            global expression
            if "^" in expression:
                expression = expression.replace("^", "**")
                total = str(eval(expression))
                if len(total) <= 6:
                    expression_field['font'] = myFont3
                equation.set(total)
                expression = total
            else:
                total = str(eval(expression))
                equation.set(total)
                expression = total


        except:
            equation.set("!!Error!!")
            expression = ""


    root.bind("<Return>", equal)


    def press(num, event=None):
        global expression
        expression = expression + str(num)
        equation.set(expression)


    root.bind("1", lambda e: press(1, None))
    root.bind("2", lambda e: press(2, None))
    root.bind("3", lambda e: press(3, None))
    root.bind("4", lambda e: press(4, None))
    root.bind("5", lambda e: press(5, None))
    root.bind("6", lambda e: press(6, None))
    root.bind("7", lambda e: press(7, None))
    root.bind("8", lambda e: press(8, None))
    root.bind("9", lambda e: press(9, None))
    root.bind("0", lambda e: press(0, None))
    root.bind("/", lambda e: press("/", None))
    root.bind("*", lambda e: press("*", None))
    root.bind("-", lambda e: press("-", None))
    root.bind("+", lambda e: press("+", None))
    root.bind(".", lambda e: press(".", None))
    root.bind("^", lambda e: press("^", None))
    root.bind("r", lambda e: press("^2", None))
    root.bind("`", lambda e: Plusminus())
    root.bind("<BackSpace>", lambda e: back())
    root.bind("<Escape>", lambda e: clear())

    # Buttons
    Btn1 = tk.Button(root, text="1", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(1))
    Btn1['font'] = myFont1
    Btn1.pack()
    Btn1.place(height=50, width=80, x=1, y=347.5)

    Btn2 = tk.Button(root, text="2", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(2), activeforeground="Black")
    Btn2['font'] = myFont1
    Btn2.pack()
    Btn2.place(height=50, width=80, x=82.5, y=347.5)

    Btn3 = tk.Button(root, text="3", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(3), activeforeground="Black")
    Btn3['font'] = myFont1
    Btn3.pack()
    Btn3.place(height=50, width=80, x=165, y=347.5)

    equal = tk.Button(root, text="= ", bg="#964c00", fg="White", border="0", activebackground="#e17100",
                      command=equal, activeforeground="White")
    equal['font'] = myFont1
    equal.pack()
    equal.place(height=50, width=80, x=247, y=400)

    Btn4 = tk.Button(root, text="4", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(4), activeforeground="Black")
    Btn4['font'] = myFont1
    Btn4.pack()
    Btn4.place(height=50, width=80, x=1, y=296)

    Btn5 = tk.Button(root, text="5", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(5), activeforeground="Black")
    Btn5['font'] = myFont1
    Btn5.pack()
    Btn5.place(height=50, width=80, x=82.5, y=296)

    Btn6 = tk.Button(root, text="6", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(6), activeforeground="Black")
    Btn6['font'] = myFont1
    Btn6.pack()
    Btn6.place(height=50, width=80, x=165, y=296)

    Add = tk.Button(root, text="+ ", bg="#000000", fg="White", border="0", activebackground="White",
                    command=lambda: press("+"), activeforeground="Black")
    Add['font'] = myFont1
    Add.pack()
    Add.place(height=50, width=80, x=247, y=347.5)

    Btn0 = tk.Button(root, text="0", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(0), activeforeground="Black")
    Btn0['font'] = myFont1
    Btn0.pack()
    Btn0.place(height=50, width=80, x=82.5, y=400)

    Decimal = tk.Button(root, text=".", bg="#000000", fg="White", border="0", activebackground="White",
                        command=lambda: press("."), activeforeground="Black")
    Decimal['font'] = myFont1
    Decimal.pack()
    Decimal.place(height=50, width=80, x=165, y=400)

    Clear = tk.Button(root, text="<=", bg="#000000", fg="White", border="0", activebackground="White",
                      command=back, activeforeground="Black")
    Clear['font'] = myFont1
    Clear.pack()
    Clear.place(height=50, width=80, x=82.5, y=191.5)

    Btn7 = tk.Button(root, text="7", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(7), activeforeground="Black")
    Btn7['font'] = myFont1
    Btn7.pack()
    Btn7.place(height=50, width=80, x=1, y=243.5)

    Btn8 = tk.Button(root, text="8", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(8), activeforeground="Black")
    Btn8['font'] = myFont1
    Btn8.pack()
    Btn8.place(height=50, width=80, x=82.5, y=243.5)

    Btn9 = tk.Button(root, text="9", bg="#000000", fg="White", border="0", activebackground="White",
                     command=lambda: press(9), activeforeground="Black")
    Btn9['font'] = myFont1
    Btn9.pack()
    Btn9.place(height=50, width=80, x=165, y=243.5)

    Subtract = tk.Button(root, text="- ", bg="#000000", fg="White", border="0", activebackground="White",
                         command=lambda: press("-"), activeforeground="Black")
    Subtract['font'] = myFont2
    Subtract.pack()
    Subtract.place(height=50, width=80, x=247, y=296)

    Multiply = tk.Button(root, text="* ", bg="#000000", fg="White", border="0", activebackground="White",
                         command=lambda: press("*"), activeforeground="Black", pady="30")
    Multiply['font'] = myFont1
    Multiply.pack()
    Multiply.place(height=50, width=80, x=247, y=243.5)

    Divide = tk.Button(root, text="/ ", bg="#000000", fg="White", border="0", activebackground="White",
                       command=lambda: press("/"), activeforeground="Black", pady="30")
    Divide['font'] = myFont1
    Divide.pack()
    Divide.place(height=50, width=80, x=247, y=191.5)

    Clearall = tk.Button(root, text="C", bg="#000000", fg="White", border="0", activebackground="White",
                         command=clear, activeforeground="Black", pady="30")
    Clearall['font'] = myFont1
    Clearall.pack()
    Clearall.place(height=50, width=80, x=165, y=191.5)
    minus = tk.Button(root, text="+/-", bg="#000000", fg="White", border="0", activebackground="White",
                      command=Plusminus, activeforeground="Black", pady="30")
    minus['font'] = myFont1
    minus.pack()
    minus.place(height=50, width=80, x=1, y=400)

    Percentage = tk.Button(root, text="x^2", bg="#000000", fg="White", border="0", activebackground="White",
                           command=lambda: press("^2"), activeforeground="Black", pady="30")
    Percentage['font'] = myFont1
    Percentage.pack()
    Percentage.place(height=50, width=80, x=1, y=191.5)

root.mainloop()
