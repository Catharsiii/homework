from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import StringVar

"1. Исключения для: деления, корня  2. Изменение знака при повторном нажатии на него, 3. "

mainw = Tk()
mainw.title("Calculator")
mainw.geometry("330x503")
mainw.configure(background="#E9E9E9")
mainw.attributes('-alpha',0.95)

mainw.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')

style.configure("TButton", font=("Courier New", 17, "bold"), background="#FFFFFF", foreground="#000000", padding=10, bordercolor="#E9E9E9", lightcolor="#F6F6F6", darkcolor="#F6F6F6")

style.configure("Opr.TButton", font=("Courier New", 17), background="#F6F6F6", foreground="#000000", padding=10, bordercolor="#E9E9E9", lightcolor="#F6F6F6", darkcolor="#F6F6F6")
lab = StringVar()
lab.set("0")

labb = ttk.Label(mainw, textvariable=lab, font=("Courier New", 40, "bold"), relief="flat", background="#E9E9E9",anchor="e")
labb.place(x=5, y=80, width=320, height=60)

def res_to_d():
    """Функция для восстановления прежнего шрифта в лейбле"""
    labb.config(font=("Courier New",40, "bold"))


def equall():
    """
    функуия, выводящая решение выражения в окне калькулятора
    """
    try:
        math_exp = lab.get()
        math_exp = (math_exp.replace(u'\u221a', "** (1 / 2)").replace('\u00D7', '*')
                    .replace('x\u00B2', "** 2").replace('\u00F7', "/")
                    .replace('\u00D7', "*").replace(",", "."))
        res = eval(math_exp)
        if res.is_integer():
            res = int(res)
        lab.set(str(round(res, 8)))
    except ZeroDivisionError:
        labb.config(font=("Courier New", 15))
        lab.set("деление на ноль невозможно")


def add_num(num):
    """
    Функция выводит значение кнопки на "экран" калькулятора
    параметры: num - цифра/операция
    """
    res_to_d()
    cur = lab.get()
    cur.replace('\u00D7', '*')


    if cur.replace(' ','').isalpha():
        lab.set(num)
    else:
        if cur == "0":
            if num == ",":
                cur += num
                lab.set(cur)
            else:
                lab.set(num)
        else:
            if len(cur) < 10:
                lab.set(cur + num)
            else:
                lab.set(cur[1:] + num)

    if cur[-1] in ("+", "-", "*", "/", "\u00D7"):
        if num in ("+", "-", "*", "/", "\u00D7"):
            if cur == "0":
                lab.set(cur + num)
            else:
                lab.set(cur[:-1] + num)


def kvadrat():
    """
    функция возводит в квадрат число на 'экране' калькулятора и выводит результат
    """
    try:
        res = lab.get()
        res = res.replace(",", ".")
        if float(res).is_integer():
            res = int(res)
        else:
            res = float(res)
        lab.set(str(round((res ** 2), 8)))
    except ValueError:
        labb.config(font=("Courier New", 15))
        lab.set("Введены неверные данные")




def percent():
    """
    функция находит процент от числа 'экране' калькулятора и выводит результат
    """
    try:
        res = lab.get()
        res = res.replace(",", ".")
        if float(res).is_integer():
            res = int(res)
        else:
            res = float(res)
        lab.set(str(round(res / 100, 8)))
    except  ValueError:
        labb.config(font=("Courier New", 15))
        lab.set("Введены неверные данные")

def sqr():
    """
    функция находит корень от числа 'экране' калькулятора и выводит результат
    """
    try:
        res = lab.get()
        res = res.replace(",", ".")
        sq = float(res) ** (1 / 2)
        if sq.is_integer():
            sq = int(sq)
        else:
            sq = float(sq)
        lab.set(str(round(sq, 8)))
    except AttributeError:
        labb.config(font=("Courier New", 15))
        lab.set("Введены неверные данные")
    except ValueError:
        labb.config(font=("Courier New", 15))
        lab.set("Введены неверные данные")

def del_1():
    """
    функция находит решение выражения 1 / x, где x - число на 'экране' калькулятора и выводит результат
    """
    try:
        res = lab.get()
        res = res.replace(",", ".")
        deln = 1 / float(res)
        if deln.is_integer():
            deln = int(deln)
        else:
            deln = float(deln)
        lab.set(str(round(deln, 8)))
    except ZeroDivisionError:
        labb.config(font=("Courier New", 15))
        lab.set("Деление на ноль невозможно")
    except ValueError:
        labb.config(font=("Courier New", 15))
        lab.set("Введены неверные данные")

def pl_min():
    """
    функция меняет знак числа на 'экране' калькулятора и выводит результат
    """
    try:
        res = lab.get()
        res = res.replace(",", ".")
        if float(res) > 0:
            res =  "-" + res
        elif float(res) < 0:
            res = res.lstrip("-")
        else:
            lab.set("0")
        res = res.replace(".", ",")
        lab.set(res)
    except ValueError:
        labb.config(font=("Courier New", 15))
        lab.set("Введены неверные данные")

def deleteall():
    """
    Функция стирает все ранее выведенные элементы с "экрана" калькулятора
    """
    res_to_d()
    lab.set("0")


def back():
    """
    Функция стирает крайний введенный на "экране" калькулятора символ
    """
    cur = lab.get()
    if len(cur) > 1:
        lab.set(cur[:-1])
    else:
        lab.set("0")

button_font = font.Font(size=20)
plus_min = ttk.Button(text='\u00B1', style="Opr.TButton", command=lambda:pl_min())
plus_min.place(x=5, y=445, width=80, height=55)
null = ttk.Button(text="0", style="TButton", command=lambda:add_num("0"))
null.place(x=85, y=445, width=80, height=55)
an = ttk.Button(text=",", style="Opr.TButton", command=lambda:add_num(","))
an.place(x=165, y=445, width=80, height=55)
equal = ttk.Button(text="=", style="Opr.TButton", command=equall)
equal.place(x=245, y=445, width=80, height=55)

one = ttk.Button(text="1", style="TButton", command=lambda:add_num("1"))
one.place(x=5, y=390, width=80, height=55)
two = ttk.Button(text="2", style="TButton", command=lambda:add_num("2"))
two.place(x=85, y=390, width=80, height=55)
three = ttk.Button(text="3", style="TButton", command=lambda:add_num("3"))
three.place(x=165, y=390, width=80, height=55)
plus = ttk.Button(text="+", style="Opr.TButton", command=lambda:add_num("+"))
plus.place(x=245, y=390, width=80, height=55)

four = ttk.Button(text="4", style="TButton", command=lambda:add_num("4"))
four.place(x=5, y=335, width=80, height=55)
five = ttk.Button(text="5", style="TButton", command=lambda:add_num("5"))
five.place(x=85, y=335, width=80, height=55)
six = ttk.Button(text="6", style="TButton", command=lambda:add_num("6"))
six.place(x=165, y=335, width=80, height=55)
minus = ttk.Button(text="-", style="Opr.TButton", command=lambda:add_num("-"))
minus.place(x=245, y=335, width=80, height=55)

seven = ttk.Button(text="7", style="TButton", command=lambda:add_num("7"))
seven.place(x=5, y=280, width=80, height=55)
eight = ttk.Button(text="8", style="TButton", command=lambda:add_num("8"))
eight.place(x=85, y=280, width=80, height=55)
nine = ttk.Button(text="9", style="TButton", command=lambda:add_num("9"))
nine.place(x=165, y=280, width=80, height=55)
perm = ttk.Button(text='\u00D7', style="Opr.TButton", command=lambda:add_num('\u00D7'))
perm.place(x=245, y=280, width=80, height=55)

delete = ttk.Button(text="CE", style="Opr.TButton", command=deleteall)
delete.place(x=5, y=225, width=80, height=55)
deletall = ttk.Button(text="C", style="Opr.TButton", command=deleteall)
deletall.place(x=85, y=225, width=80, height=55)
back = ttk.Button(text='⌫', style="Opr.TButton", command=back)
back.place(x=165, y=225, width=80, height=55)
delen = ttk.Button(text='\u00F7', style="Opr.TButton", command=lambda:add_num('/'))
delen.place(x=245, y=225, width=80, height=55)

per = ttk.Button(text="%", style="Opr.TButton", command=percent)
per.place(x=5, y=170, width=80, height=55)
sqrt = ttk.Button(text=u'\u221a', style="Opr.TButton", command=sqr)
sqrt.place(x=85, y=170, width=80, height=55)
kv = ttk.Button(text='x\u00B2', style="Opr.TButton", command=kvadrat)
kv.place(x=165, y=170, width=80, height=55)
delna1 = ttk.Button(text='1/x', style="Opr.TButton", command=del_1)
delna1.place(x=245, y=170, width=80, height=55)

mainw.mainloop()
