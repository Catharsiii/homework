import math

def f(x):
    return math.sin(x)
import tkinter as tk
mainm = tk.Tk()
mainm.title('наше окно')
mainm.geometry('1000x1000')

def f(x):
    return math.sin(x)
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


def checking_func(func, a, b, center_x, center_y, scale, e = 10 ** (-5)):
    '''
    Функция находит точки пересечения заданной функции с осью абсцисс
    аргументы:
    func - заданная функция
    a, b - отезок исследования функции
    e - бесконечно малое число
    вывод:
    None - если метод дихотомии не может быть применен к данному отрезку
    строка - если хотя бы один корень был найден
    '''
    if func(a) * func(b) >= 0:
        print("Метод дихотомии не может быть применен на данном интервале")
        return None
    
    canv.create_line(center_x + a * scale, center_x - 200, center_x + a * scale, center_y + 200, dash = 2)
    canv.create_line(center_x + b * scale, center_y - 200, center_x + b * scale, center_y + 200, dash = 2)
    
    while (b - a) / 2.0 > e:
        c = (a + b) / 2.0
        canv.create_line(center_x + c * scale, center_y + 25, center_x + c * scale, center_y - 25)
        if func(c) == 0:
            return c  # Найден корень
        elif func(a) * func(c) < 0:
            b = c  # Корень в левом подинтервале
        else:
            a = c  # Корень в правом подинтервале
    return (a + b) / 2.0  # Возвращаем приближенное значение корня
a = 12.57
b = 15.71

s = 50
canv = tk.Canvas(width = 1000, height = 1000, bg='white') # создание белого холста размером 1000*800
canv.pack()
drow_func(f, 7, 10, 500, 500, 30, 'blue')
create_dpsk(1000, 1000, 500, 500, 30, 800, 800, 'black', 'black')
check = checking_func(f, 7, 10, 500, 500, 30)
if check is not None:
    print(f"Корень функции заданной на отрезке [{a}, {b}] равен: {check}")
tk.mainloop()

