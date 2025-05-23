import math
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import StringVar
mainw = tk.Tk()
mainw.title("График")
mainw.geometry("900x700")
mainw.configure(background="#E9E9E9", highlightthickness= 3, highlightbackground = 'black')
mainw.resizable(False, False)

canv = tk.Canvas(width=680, height=660, bg='white', highlightthickness= 3, highlightbackground = "#474A51")

scale_var = tk.DoubleVar()
scale_var.set(30)
# функции для всего

def create_axes(width: int, height: int, center_x: int, center_y: int, length_x, length_y, color_x, color_y):
    """
        функция для построения осей Декартовой прямоугольной системы координат
        param: width - ширина холста
               height - высота холста
               center_x - центр оси абсцисс
               center_y - центр оси ординат
               length_x - длина оси абсцисс
               length_y - длина оси ординат
               color_x - цвет оси абсцисс
               color_y - цвет оси ординат
    """
    beg_x = (width - length_x) // 2
    canv.create_line(beg_x, center_y, beg_x + length_x, center_y, fill=color_x, arrow='last')
    beg_y = (height - length_y) // 2
    canv.create_line(center_x, beg_y, center_x, beg_y + length_y, fill=color_y, arrow='first')


def create_scale(center_x, center_y, scale, length_x, length_y):
    """
        функция для построения отсечек на осях и названия осей
        param: center_x - центр оси абсцисс
               center_y - центр оси ординат
               scale - единичный отрезок
               length_x - длина оси абсцисс
               length_y - длина оси ординат
    """
    width = int(canv.__getitem__('width'))
    height = int(canv.__getitem__('height'))
    beg_x = (width - length_x) // 2  # расстояние от начала полотна до начала оси абсцисс
    start = center_x - beg_x
    n = (length_x - start) // scale  # отсечки на '+'
    m = start // scale  # отсечки на '-'
    for i in range(n):
        canv.create_line(center_x + i * scale, center_y + 3, center_x + i * scale, center_y - 3)
    for i in range(m):
        canv.create_line(center_x - i * scale, center_y + 3, center_x - i * scale, center_y - 3)
    beg_y = (height - length_y) // 2
    start_y = center_y - beg_y
    plus_oy = start_y // scale
    min_oy = (length_y - start_y) // scale
    for i in range(plus_oy):
        canv.create_line(center_x + 3, center_y - i * scale, center_x - 3, center_y - i * scale)
    for i in range(min_oy):
        canv.create_line(center_x + 3, center_y + i * scale, center_x - 3, center_y + i * scale)
    for i in range(5 * n):
        canv.create_line(center_x + i * (scale / 5), center_y + 2, center_x + i * (scale / 5), center_y - 2)
    for i in range(m * 5):
        canv.create_line(center_x - i * (scale / 5), center_y + 2, center_x - i * (scale / 5), center_y - 2)
    for i in range(5 * plus_oy):
        canv.create_line(center_x + 1.5, center_y - i * (scale / 5), center_x - 1.5, center_y - i * (scale / 5))
    for i in range(5 * min_oy):
        canv.create_line(center_x + 1.5, center_y + i * (scale / 5), center_x - 1.5, center_y + i * (scale / 5))

    for i in range(n):
        canv.create_text(center_x + (i + 1) * scale, center_y + 10, text=str(i + 1))
    for i in range(m):
        canv.create_text(center_x - (i + 1) * scale, center_y + 10, text=str(-i - 1))

    for i in range(plus_oy):
        canv.create_text(center_x - 10, center_y - (i + 1) * scale, text=str(i + 1))
    for i in range(min_oy):
        canv.create_text(center_x - 10, center_y + (i + 1) * scale, text=str(-i - 1))

    canv.create_text(center_x - scale / 3, center_y + scale / 2, text='0')
    canv.create_text(center_x + length_x / 2 + scale / 3, center_y + scale, text='X')
    canv.create_text(center_x - scale * 1.5, center_y - length_y / 2 + 10, text='Y')


def create_dpsk(width: int, height: int, center_x: int, center_y: int, scale: int, length_x, length_y, color_x,
                color_y):
    """
        функция для создания Декартовой прямоугольной системы координат
        param: width - ширина холста
               height - высота холста
               center_x - центр оси абсцисс
               center_y - центр оси ординат
               scale - единичный отрезок
               length_x - длина оси абсцисс
               length_y - длина оси ординат
               color_x - цвет оси абсцисс
               color_y - цвет оси ординат
    """
    create_axes(width, height, center_x, center_y, length_x, length_y, color_x, color_y)
    create_scale(center_x, center_y, scale, length_x, length_y)


def drow_func(func, a, b, center_x, center_y, scale, color_f='black'):
    """
        Функция для построения графика заданной функции
        аргументы: func - заданная функция
                   a, b - отрезок исследования функции
                   center_x - центр оси абсцисс
                   center_y - центр оси ординат
                   scale - единичный отрезок
                   color_f -цвет графика (по умолчанию черный)

    """
    length = b - a
    h = 0.01
    steps = int(length / h)
    for i in range(steps - 1):
        x0 = (a + i * h) * scale
        y0 = func(a + i * h) * scale
        x1 = (a + (i + 1) * h) * scale
        y1 = func(a + (i + 1) * h) * scale
        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1, fill=color_f)

def draw_function():
    canv.delete("all")

    try:
        func_str = func_entr.get()
        func = lambda x: eval(func_str, {'math': math, 'x': x})
        current_scale = scale_var.get()
        drow_func(func, -10, 10, 340, 330, current_scale, 'blue')
        create_dpsk(680, 660, 340, 330, int(round(current_scale, 0)), 650, 650, "black", "black")
    except Exception as excep:
        print(f"Ошибка: {excep}")


lab0 = ttk.Label(mainw, text="Меню", font=("Courier New", 20, "bold"), relief="flat", foreground="#474A51", background="#E9E9E9",anchor="e")
lab0.place(x=30, y=10, width=100, height=30)

style = ttk.Style()
style.theme_use('winnative')

style.configure("Custom.Horizontal.TScale", background="#E9E9E9", troughcolor="#474A51", sliderthickness=5, gripcount=0, troughrelief='flat', sliderrelief='flat', slidercolor='black')

scale = ttk.Scale(mainw, from_=0, to=100, length=300, style="Custom.Horizontal.TScale")
scale.place(x=44, y=95, width=100, height=30)
lab_sc_0 = ttk.Label(mainw, text="0", font=("Courier New", 10, "bold"), relief="flat", background="#E9E9E9", anchor="e")
lab_sc_0.place(x=43, y=115)
lab1 = ttk.Label(mainw, text="Масштаб", font=("Courier New", 15, "bold"), relief="flat", foreground="#474A51", background="#E9E9E9",anchor="e")
lab1.place(x=7, y=60, width=100, height=30)

lab2 = ttk.Label(mainw, text="Функция", font=("Courier New", 15, "bold"), foreground="#474A51", relief="flat", background="#E9E9E9",anchor="e")
lab2.place(x=7, y=140, width=100, height=30)



style.configure("MyEntry.TEntry", fieldbackground="white", relief="flat", foreground="black", font=("Courier New", 20, "bold"), lightcolor="black", darkcolor="black", bordercolor="black", padding=5)

func_entr = ttk.Entry(mainw, style="MyEntry.TEntry")
func_entr.place(x=47, y=185, width=100, height=30)

style.configure("TButton", font=("Courier New", 13, "bold"), relief="solid", foreground="#474A51", background="#E9E9E9",anchor="n")

lab_dr = ttk.Button(mainw, text="Рисовать", style="TButton", command=draw_function)
lab_dr.place(x=47, y=220, width=100, height=30)

lab_ypr = ttk.Label(mainw, text="Управление\nграфиком", font=("Courier New", 15, "bold"), relief="flat", foreground="#474A51", background="#E9E9E9",anchor="n")
lab_ypr.place(x=0, y=270, width=150, height=70)

# кнопки сдвига
rigth = ttk.Button(mainw, text="→", style="TButton")
rigth .place(x=47, y=340, width=100, height=40)

left = ttk.Button(mainw, text="←", style="TButton")
left.place(x=47, y=390, width=100, height=40)

up = ttk.Button(mainw, text='↑', style="TButton")
up.place(x=47, y=440, width=100, height=40)

down = ttk.Button(mainw, text="↓", style="TButton")
down.place(x=47, y=490, width=100, height=40)


draw_function()
canv.place(x=190, y=15)

mainw.mainloop()
