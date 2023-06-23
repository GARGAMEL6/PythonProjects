import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    if calc.get() == '0' and len(calc.get()) == 1 or calc.get() == '0.0':
        value = digit
    else:
        value = calc.get() + digit
    calc.delete(0, tk.END)
    calc.insert(0, value)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/' and operation not in '()':
        value = value[:-1]
    elif ('+' in value or '-' in value or '*' in value or '/' in value) and operation not in '()':
        calculate()
        value = calc.get()
    elif (calc.get() == '0' or calc.get() == '0.0') and (operation in '()'):
        value = ''
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    result = 0
    value = calc.get()
    if value[-1] in '+-*/':
        value += value[:-1]
    calc.delete(0, tk.END)
    try:
        result = eval(value)
        if int(result) == result:
            calc.insert(0, int(result))
        else:
            calc.insert(0, result)
    except (NameError, SyntaxError):
        messagebox.showerror('Error', 'Вводите только цифры или закройте скобки!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Не дели на 0!')
        calc.insert(0, 0)


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(win, text=digit, bd=5, bg='#000000', fg='#FFFFFF', font=('Calibri', 24),
                     activebackground='#000000', activeforeground='#FFFFFF', command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(win, text=operation, bd=5, bg='#000000', fg='yellow', font=('Calibri', 24),
                     activebackground='#000000', activeforeground='yellow', command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(win, text=operation, bd=5, bg='#000000', fg='yellow', font=('Calibri', 24),
                     activebackground='#000000', activeforeground='yellow', command=calculate)


def make_clear_button(operation):
    return tk.Button(win, text=operation, bd=5, bg='#000000', fg='yellow', font=('Calibri', 24),
                     activebackground='#000000', activeforeground='yellow', command=clear)


def make_sqr_button(operation):
    return tk.Button(win, text=operation, bd=5, bg='#000000', fg='yellow', font=('Calibri', 24),
                     activebackground='#000000', activeforeground='yellow', command=lambda: add_operation('**2'))


def make_sqrt_button(operation):
    return tk.Button(win, text=operation, bd=5, bg='#000000', fg='yellow', font=('Calibri', 24),
                     activebackground='#000000', activeforeground='yellow', command=lambda: add_operation('**0.5'))


win = tk.Tk()
win['bg'] = '#000000'
win.title('Калькулятор')
win.geometry("550x450+100+200")
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Calibry', 18), bg='#000000', fg='#FFFFFF')
calc.insert(0, '0')
calc.grid(row='0', column='0', columnspan=5, stick='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_operation_button('(').grid(row=3, column=4, stick='wens', padx=5, pady=5)
make_operation_button(')').grid(row=4, column=4, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_sqr_button('Квадрат').grid(row=1, column=4, stick='wens', padx=5, pady=5)
make_sqrt_button('Корень').grid(row=2, column=4, stick='wens', padx=5, pady=5)

win.grid_rowconfigure(1, minsize=100)
win.grid_rowconfigure(3, minsize=100)
win.grid_rowconfigure(2, minsize=100)
win.grid_rowconfigure(4, minsize=100)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=100)

win.mainloop()
