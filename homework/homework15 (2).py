import math
#1. Написать функцию вычисления значения функции в заданной точке и обозначения этой пары на графике функции
import tkinter as tk
mainm = tk.Tk()
mainm.title('окно')
mainm.geometry('1000x1000')




#2.Написать функцию поиска максимума и минимума функции, а также точек максимума и минимума  на заданном отрезке.
    #Найденные точки обозначить на графике функции разными цветами
#3. Написать функцию, рисующую график функции так, чтобы промежутки возрастания и
    #убывания функции были нарисованы разными цветами
#4. При написании функций продумать обработку возможных ошибок



def create_axes(width: int, height: int, center_x: int, center_y: int, scale: int, length_x, length_y, color_x, color_y):
    '''

    '''
    beg_x = (width - length_x) // 2
    canv.create_line(beg_x, center_y, beg_x + length_x, center_y, fill=color_x, arrow = 'last')
    beg_y = (height - length_y) // 2
    canv.create_line(center_x, beg_y, center_x, beg_y + length_y, fill = color_y, arrow = 'first')

    
def create_scale(center_x, center_y, scale, length_x, length_y):
    width = int(canv.__getitem__('width'))
    height = int(canv.__getitem__('height'))
    beg_x = (width - length_x) // 2 # расстояние от начала полотна до начала оси абсцисс
    start = center_x - beg_x
    n = (length_x - start) // scale # отсечки на '+'
    m = start // scale # отсечки на '-'
    for i in range (n):
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
    for i in range (5 * plus_oy):
        canv.create_line(center_x + 1.5, center_y - i* (scale / 5), center_x - 1.5,  center_y - i * (scale / 5))
    for i in range (5 * min_oy):
        canv.create_line(center_x + 1.5, center_y + i * (scale / 5), center_x - 1.5,  center_y + i * (scale / 5))
        
    for i in range(n):
        canv.create_text(center_x + (i + 1) * scale,  center_y + 10, text=str(i + 1))
    for i in range(m):
        canv.create_text(center_x - (i + 1) * scale, center_y + 10, text=str(-i - 1))

    for i in range(plus_oy):
        canv.create_text(center_x - 10, center_y - (i + 1) * scale, text=str(i + 1))
    for i in range(min_oy):
        canv.create_text(center_x - 10, center_y + (i + 1) * scale, text=str(-i - 1))        

    canv.create_text(center_x - scale / 3, center_y + scale / 2, text='0')
    canv.create_text(center_x + length_x / 2 + scale / 2, center_y + scale * 1.5, text='X')
    canv.create_text(center_x - scale * 1.5, center_y - length_y / 2, text='Y')

def create_dpsk(width: int, height: int, center_x: int, center_y: int, scale: int, length_x, length_y, color_x, color_y):
    create_axes(width, height, center_x, center_y, scale, length_x, length_y, color_x, color_y)
    create_scale(center_x, center_y, scale, length_x, length_y)

def f(x):
    return math.cos(x)
    
def drow_func(func, a, b, center_x, center_y, scale, color_f = None):
    length = b - a
    h = 0.01
    steps = int(length / h)
    for i in range (steps - 1):
        x0 = (a + i * h) * scale
        y0 = func(a + i * h) * scale
        x1 = (a + (i + 1) * h) * scale
        y1 = func(a + (i + 1) * h)* scale
        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1, fill = color_f)

s = 50
canv = tk.Canvas(width = 1000, height = 1000, bg='white')
canv.pack()
drow_func(f, -10, 10, 500, 500, 30, 'red')
create_dpsk(1000, 1000, 500, 500, 30, 800, 800, 'black', 'black')
tk.mainloop()

