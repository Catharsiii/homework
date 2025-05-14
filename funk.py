'''
    Рисование графиков
'''
import tkinter as tk
import math
from audioop import minmax
from shutil import which

xgeom = 1000
ygeom = 800
mainm = tk.Tk()
mainm.title('наше окно')
mainm.geometry(str(xgeom) + 'x' + str(ygeom))


def drawScale(isVertical: int = 1, scale: int = 10, center_x: int = 500, center_y: int = 400, length: int = 500):
    '''
    функция рисует шкалу на оси
        :param isVertical - признак вертикальная ось: 1 или горизонтальная: 0
        :param scale - масштаб
        :param length - длина оси
        :param center_x - x координата центра системы координат
        :param center_x - x координата центра системы координат
     '''
    width = int(canv.__getitem__('width'))  # узнали шириину полотна
    height = int(canv.__getitem__('height'))  # узнали высоту полотна
    if isVertical == 0:  # отчсечки на горизонтальной оси
        x_shift = (width - length) // 2
        start = center_x - x_shift
        n = (length - start) // scale  # количество отсечек на  положительной части оси x
        m = (start) // scale  # количество отсеек на отрицательной части оси x
        for i in range(n):
            canv.create_line(center_x + i * scale, center_y - 5, center_x + i * scale, center_y + 5, width = 3)
            if i != 0:
                canv.create_text(center_x +i*scale, center_y + 12, text=i*1)
        for i in range(m):
            canv.create_line(center_x - i * scale, center_y - 5, center_x - i * scale, center_y + 5, width = 3)
            if i != 0:
                canv.create_text(center_x -i*scale, center_y + 12, text=i*-1)
    else:  # отчсечки на вертикальной оси
        y_shift = (height - length) // 2
        start = center_y - y_shift
        n = (length - start) // scale  # количество отсеек на отрицательной части оси y
        m = (start) // scale  # количество отсечек на  положительной части оси y
        for i in range(n):
            canv.create_line(center_x + 5, center_y + i * scale, center_x - 5, center_y + i * scale, width = 3)
            if i != 0:
                canv.create_text(center_x + 12, center_y + i*scale, text=i*-1)
        for i in range(m):
            canv.create_line(center_x + 5, center_y - i * scale, center_x - 5, center_y - i * scale, width = 3)
            if i != 0:
                canv.create_text(center_x + 12, center_y - i*scale, text=i)




def drawScal(isVertical: int = 1, scale: int = 10, center_x: int = 500, center_y: int = 400, length: int = 500):
    '''
    функция рисует шкалу на оси
        :param isVertical - признак вертикальная ось: 1 или горизонтальная: 0
        :param scale - масштаб
        :param length - длина оси
        :param center_x - x координата центра системы координат
        :param center_x - x координата центра системы координат
     '''
    width = int(canv.__getitem__('width'))  # узнали шириину полотна
    height = int(canv.__getitem__('height'))  # узнали высоту полотна
    if isVertical == 0:  # отчсечки на горизонтальной оси
        n = (xgeom ) // scale
        for i in range(n):
            canv.create_line(center_x + i * scale, center_y - ygeom, center_x + i * scale, center_y + ygeom)

        for i in range(n):
            canv.create_line(center_x - i * scale, center_y - ygeom, center_x - i * scale, center_y + ygeom)
    else:  # отчсечки на вертикальной оси
        n = (ygeom) // scale  # количество отсеек на отрицательной части оси y
        for i in range(n):
            canv.create_line(center_x + xgeom, center_y + i * scale, center_x - xgeom, center_y + i * scale)
        for i in range(n):
            canv.create_line(center_x + xgeom, center_y - i * scale, center_x - xgeom, center_y - i * scale)



def drawAxe(isVertical: int = 1, length: int = 500, isNeededLines: bool = False, width: int = xgeom, height: int = ygeom,
            center_x: int = 500, center_y: int = 400, scale: int = 10):
    '''
    функция рисует ось координат (горизонтальную или вертикальную)

        :param isVertical - признак вертикальная ось: 1 или горизонтальная: 0
        :param length - длина оси
        :isNeededLines - нужна ли шкала на оси
        :param center_x = координата центра координат по x
        :param center_y = координата центра координат по y
        :param scale - масштаб
        :param width: - ширина полотна
        :param height: - высота полотна
    '''
    if isVertical:
        y_shift = (height - length) // 2
        canv.create_line(center_x, y_shift, center_x, y_shift + length, arrow='first', width = 3)
        drawScale(1, scale, center_x, center_y, length)
        drawScal(1, scale, center_x, center_y, length)
    else:
        x_shift = (width - length) // 2

        canv.create_line(x_shift, center_y, x_shift + length, center_y, arrow='last', width = 3)
        drawScale(0, scale, center_x, center_y, length)
        drawScal(0, scale, center_x, center_y, length)

def create_dpsk(axesx: int = 1, axesy: int = 1, scale: int = 10, width: int = 1000, height: int = 800,
                center_x: int = 500, center_y: int = 400):
    '''
        Функция рисует Декартову систему координат на плокости
        :param axesx: - наличие осей координат Оx 0 - нет, 1 -есть
        :param axesy: - наличие осей координат Оy 0 - нет, 1 -есть
        :param scale: - масштаб
        :param width: - ширина полотна
        :param height: - высота полотна
        :param center_x = координата центра координат по x
        :param center_y = координата центра координат по y

    '''
    drawAxe(center_x=center_x, center_y=center_y, scale=s)
    drawAxe(center_x=center_x, center_y=center_y, scale=s, isVertical=0, length=800)




def f(x):
    '''
        Функция
    '''
    return 5*math.sin(x)

def draw_func(func, a: int, b: int, scale, center_x, center_y, clour, wid: int = 3):
    '''

    '''
    length = b - a  # длина отрезка
    h = 0.01  # шаг для рисования графика функции
    n = int(length / h)
    for i in range(n - 1):
        x0 = (a + i * h) * scale
        y0 = func(a + i * h) * scale
        x1 = (a + (i + 1) * h) * scale
        y1 = func(a + (i + 1) * h) * scale
        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1,  fill=clour, width=wid)

s = 50
canv = tk.Canvas(width=1000, height=800, bg='white')
canv.pack()
create_dpsk(center_x=400, center_y=400, scale=s)
draw_func(f, -8, 8, center_x=400, center_y=400, scale=s, clour='#FF0000', wid=3)




'''1.	Написать функцию вычисления значения функции в заданной точке и обозначения этой пары на графике функции'''
def g(x, col):
    draw_func(f, x-0.05, x+0.05, center_x=400, center_y=400, scale=s, clour=col, wid=10)



g(1, '#0000FF')



'''2.	Написать функцию поиска максимума и минимума функции, а также точек максимума и минимума  
на заданном отрезке. Найденные точки обозначить на графике функции разными цветами'''
def maxmin(a, b, t):
    """
    функция принимает 
    а - левый конец отрезка
    b - прафый конец отрезка
    """
    e = a
    lst_min = []
    lst_max = []
    while e <= b:
        if f(e) < f(e+0.01) and f(e) < f(e-0.01):
            lst_min += [e]
        elif f(e) > f(e+0.01) and f(e) > f(e-0.01):
            lst_max += [e]
        e += 0.01
    if t == 1:
        for i in lst_max:
            g(i, '#000000')
    elif t == 0:
        for i in lst_min:
            g(i, '#008888')
    else:
        for i in lst_max:
            g(i, '#000000')
        for i in lst_min:
            g(i, '#008888')



maxmin(0,8, 3)



'''3.	Написать функцию, рисующую график функции так, чтобы промежутки возрастания и убывания функции были нарисованы разными цветами'''
def colour_line(a, b, col1, col2):

    """
    функция принимает 
    а - левый конец отрезка
    b - прафый конец отрезка
    col1 - цвет возростания функции 
    col2 - цвет убывания функции
    """

    lst = []
    e = a
    while e <= b:
        if f(e) < f(e+0.01) and f(e) < f(e-0.01):
            lst += [e]
        elif f(e) > f(e+0.01) and f(e) > f(e-0.01):
            lst += [e]
        e += 0.01

    for i in range(len(lst)-1):
        if i % 2 != 0:
             draw_func(f, lst[i], lst[i+1], center_x=400, center_y=400, scale=s, clour=col2, wid=3)
        else:
           draw_func(f, lst[i], lst[i+1], center_x=400, center_y=400, scale=s, clour=col1, wid=3)
colour_line(-8, 8, '#00FF00', '#0000FF')











tk.mainloop()