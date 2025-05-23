'''
    Рисование графиков
'''
import tkinter as tk
import math 
mainm = tk.Tk()
mainm.title('наше окно')
mainm.geometry('1000x800')



def drawScale(isVertical: int = 1, scale: int = 10, center_x: int = 500, center_y: int = 400,length: int = 500):
    '''
    функция рисует шкалу на оси
        :param isVertical - признак вертикальная ось: 1 или горизонтальная: 0
        :param scale - масштаб
        :param length - длина оси
        :param center_x - x координата центра системы координат
        :param center_x - x координата центра системы координат
     '''
    width = int(canv.__getitem__('width') )  # узнали ширину полотна
    height = int(canv.__getitem__('height') )  # узнали высоту полотна
    if isVertical == 0:     # отчсечки на горизонтальной оси
        x_shift = (width-length)//2 # нахождение начала оси абсцисс
        start = center_x - x_shift # начало оси абсцисс
        n = (length-start) // scale # количество отсечек на положительной части оси x
        m = (start)// scale  # количество отсеек на отрицательной части оси x
        for i in range(n):
            canv.create_line(center_x + i*scale, center_y - 5, center_x + i*scale,  center_y + 5)
            canv.create_text(center_x + (i + 1) * scale, center_y + 13, text=str(i+1))
        for i in range(m):
            canv.create_line(center_x - i*scale, center_y - 5, center_x - i*scale,  center_y + 5)
            canv.create_text(center_x - (i + 1) * scale, center_y + 13, text=str((-1 * i) - 1))
        # нанесение отсечек на оси абсцисс
        for i in range (n * 5):
            canv.create_line(center_x + i * (scale / 5), center_y + 2, center_x + i * (scale / 5), center_y - 2)
        for i in range(m * 5):
            canv.create_line(center_x - i * (scale / 5), center_y + 2, center_x - i * (scale / 5), center_y - 2)
        # нумерация отсечек
        
    else:     # отчсечки на вертикальной оси
        y_shift = (height-length)//2 # нахождение начала оси ординат
        start = center_y - y_shift #началот оси ординат 
        n = (length-start)//scale     # количество отсеек на отрицательной части оси y
        m = (start)// scale      # количество отсечек на  положительной части оси y
        for i in range(n):
            canv.create_line(center_x + 5, center_y + i * scale, center_x - 5,  center_y + i * scale)
            canv.create_text(center_x - 13 , center_y - (i + 1) * scale, text=str(i + 1))
        for i in range(m):
            canv.create_line(center_x + 5, center_y - i * scale, center_x - 5,  center_y - i * scale)
            canv.create_text(center_x - 13 , center_y + (i + 1) * scale, text=str(-1 * i - 1))
        # нанесение отсечек на оси ординат
        for i in range(n * 5):
            canv.create_line(center_x + 2, center_y + i * (scale / 5), center_x - 2,  center_y + i * (scale / 5))
        for i in range(m * 5):
            canv.create_line(center_x + 2, center_y - i* (scale / 5), center_x - 2,  center_y - i * (scale / 5))


def drawAxe(isVertical: int = 1, length: int = 500, isNeededLines: bool = False, width: int = 1000, height: int = 800, center_x: int = 500, center_y: int = 400, scale: int = 10):
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
        y_shift = (height-length)//2 # начало оси ординат
        canv.create_line(center_x, y_shift, center_x, y_shift + length, arrow = 'first') # построение оси
        drawScale(1, scale, center_x,center_y, length) # вызов функции для нанесения штрихов на ось
    else:
        x_shift = (width-length)//2 # начало оси абсцисс
        
        canv.create_line(x_shift, center_y, x_shift + length, center_y, arrow = 'last') # построение оси
        drawScale(0, scale, center_x, center_y, length) # вызов функции для нанесения штрихов на ось
        
    

def create_dpsk(axesx: int = 1, axesy: int = 1, scale: int = 10, width: int = 1000, height: int = 800, center_x: int = 500, center_y: int = 400):
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
    drawAxe(center_x=center_x, center_y=center_y, scale = scale)# вызов функции для построения оси ординат
    drawAxe(center_x=center_x,center_y=center_y, scale=scale, isVertical=0,length=800) # вызов функции для построения оси абсцисс

def f(x):
    '''
        Функция, график которой мы строим
    '''
    return math.cos(x)
def fi(x):
    return math.tan(x)

'''def func():
    a = 3
    fi = 0
    sc = 20
    while fi <= (2*math.pi):
        i = 2 * math.sqrt(a) * math.cos(2 * fi)
        if i >= 0:
            ro = math.sqrt((2 * math.sqrt(a) * math.cos(2 * fi)))
            x = sc * ro * math.cos(fi)
            y = sc * ro * math.sin(fi)
            canv.create_oval(300+x,300-y,300+x,300-y,fill = "blue")
            fi = fi + math.pi / 1800'''
            


def draw_func(func, a: int, b: int, scale, center_x, center_y, color_f: str): 
    ''' 
     Функция строит график по заданной математической функции   
    '''
    length = b - a   # длина отрезка
    h = 0.01         # шаг для рисования графика функции
    n = int(length / h) #количество шагов
    for i in range(n-1):
        x0 =  (a+i*h)*scale # нахождение абсциссы предыдущей точки 
        y0 =  func(a+i*h)*scale # нахождение ординаты предыдущей точки 
        x1 = (a+(i+1)*h)*scale # нахождение абсциссы последующией точки 
        y1 =  func(a+(i+1)*h)*scale # нахождение ординаты последующей точки
        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1, fill = color_f, width= 2) # построение графика по заданным 

def dr_l(func, f1, f2, center_x, center_y, scale, color_h):
    h = 0.01
    a = (math.fabs(f1) + math.fabs(f2)) * math.sqrt(2) / 2 # радиус описанной вокруг лемнискаты окружности с центром в начале отсчета
    length = 2 * a   # длина отрезка
    h = 0.01         # шаг для рисования графика функции
    n = int(length / h) # количество шагов
    for i in range(n - 1):
        x0 =  (f1+i*h)*scale # нахождение абсциссы предыдущей точки 
        y0 =  (f1+i*h)*scale # нахождение ординаты предыдущей точки 
        x1 = (f1+(i+1)*h)*scale # нахождение абсциссы последующией точки 
        y1 =  (f1+(i+1)*h)*scale # нахождение ординаты последующей точки
        canv.create_arc(center_x + x0, center_y - y0, center_x - x1, center_y + y1, style=tk.ARC, fill = color_h, width= 2)

s = 60
canv = tk.Canvas(width = 1000, height = 800, bg='white') # создание белого холста размером 1000*800
canv.pack()
draw_func(f, -6, 7, s, 400, 400, 'blue')
create_dpsk(center_x=400, center_y=400, scale=s) # вызов функции, создающей дпск
dr_l(f, -1, 1, center_x=400, center_y=400, scale=s, color_h='blue')
tk.mainloop()
