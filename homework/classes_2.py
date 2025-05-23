"""
1. Создать абстрактный класс Figure (на плоскости) с методами вычисления площади и периметра,
а также методом, выводящим информацию о фигуре на экран. Создать подклассы:
Rectangle (прямоугольник), Circle (круг), Triangle (треугольник) со своими
методами вычисления площади и периметра. Создать список из n фигур и вывести
полную информацию о фигурах на экран.
"""
from abc import ABC, abstractmethod
import math
import tkinter as tk
mainm = tk.Tk()
mainm.title('наше окно')
mainm.geometry('1000x1000')


def create_axes(width: int, height: int, center_x: int, center_y: int, scale: int, length_x, length_y, color_x, color_y):
    """

    """
    beg_x = (width - length_x) // 2
    canv.create_line(beg_x, center_y, beg_x + length_x, center_y, fill=color_x, arrow='last')
    beg_y = (height - length_y) // 2
    canv.create_line(center_x, beg_y, center_x, beg_y + length_y, fill=color_y, arrow='first')


def create_scale(center_x, center_y, scale, length_x, length_y):
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
    canv.create_text(center_x + length_x / 2 + scale / 2, center_y + scale * 1.5, text='X')
    canv.create_text(center_x - scale * 1.5, center_y - length_y / 2, text='Y')


def create_dpsk(width: int, height: int, center_x: int, center_y: int, scale: int, length_x, length_y, color_x, color_y):
    create_axes(width, height, center_x, center_y, scale, length_x, length_y, color_x, color_y)
    create_scale(center_x, center_y, scale, length_x, length_y)


class Figure(ABC):
    """
    Aбстрактный класс Figure (на плоскости) с методами вычисления площади и периметра и методом, выводящим информацию о фигуре на экран
    """
    @abstractmethod
    def square(self):
        """
        метод для нахождения площади фигуры
        """
        pass
    @abstractmethod
    def perimeter(self):
        """
        метод для нахождения периметра фигуры
        """
        pass
    @abstractmethod
    def inform(self):
        """
        метод для вывода информации на экран
        """
        pass
class Rectangle(Figure):
    """
    класс
    """
    def __init__(self, first_p, second_p, center_x = None, center_y = None, scale = None, color = None):
        """
        Конструктор экземпляра
        аргументы: first_p - первая вершина прямоугольника
                   second_p - вторая вершина прямоугольника
                   center_x - центр оси абсцисс
                   center_y - центр оси ординат
                   scale - масштаб
                   color - цвет заливки фигуры

        """
        self.point_1 = first_p
        self.point_2 = second_p
        coord = second_p[1]
        coord_x = second_p[0]
        second_p[1] = first_p[1]
        self.width = (sum(x ** 2 for x in (list(map(lambda  x, y: y - x, first_p, second_p))))) ** 0.5
        second_p[1] = coord
        second_p[0] = first_p[0]
        self.height = (sum(x ** 2 for x in (list(map(lambda  x, y: y - x, second_p, first_p ))))) ** 0.5
        second_p[0] = coord_x
        if center_x is not None:
            self.center_x = center_x
        if center_y is not None:
            self.center_y = center_y
        if scale is not None:
            self.scale = scale
        if color is not None:
            self.color = color
    def square(self):
        """
        метод для нахождения площади прямоугольника
        """
        self.square = round(self.width * self.height, 3)
        return self.square
    def perimeter(self):
        """
        метод для нахождения периметра прямоугольника 
        """
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
    def draw(self):
        """
        метод для построения заданного прямоугольника
        """
        if hasattr(rec, 'center_x') == True and hasattr(rec, 'center_y') == True and hasattr(rec, 'scale') == True:
            if hasattr(rec, 'color'):
                canv.create_rectangle(self.center_x + self.point_1[0] * self.scale, self.center_y - self.point_1[1] * self.scale,
                                      self.center_x + self.point_2[0] * self.scale, self.center_y - self.point_2[1] * self.scale, fill = self.color)
            else:
                canv.create_rectangle(self.center_x + self.point_1[0] * self.scale, self.center_y - self.point_1[1] * self.scale,
                                      self.center_x + self.point_2[0] * self.scale, self.center_y - self.point_2[1] * self.scale)
            canv.create_text(self.center_x + self.point_1[0] * self.scale - 6, self.center_y - self.point_1[1] * self.scale + 6, text='A')
            canv.create_text(self.center_x + self.point_2[0] * self.scale + 6, self.center_y - self.point_1[1] * self.scale + 6, text='D')
            canv.create_text(self.center_x + self.point_1[0] * self.scale - 6, self.center_y - self.point_2[1] * self.scale - 6, text='B')
            canv.create_text(self.center_x + self.point_2[0] * self.scale + 6, self.center_y - self.point_2[1] * self.scale - 6, text='A')

    def inform(self):
        """
        метод для вывода информации о данном прямоугольнике на экран
        """
        d = '\n'
        print(f'Информация о данном прямоугольнике {d} высота: {self.height} {d}ширина: {self.width}{d}площадь: {self.square}{d}периметр: {self.perimeter}')

class Circle(Figure):
    def __init__(self, center, radius, center_x = None, center_y = None, scale = None, color = None):
        """
        Конструктор экземпляра
        аргументы: center - координаты центра окружности
                   radius - координаты радиуса окружности
                   center_x - центр оси абсцисс
                   center_y - центр оси ординат
                   scale - масштаб
                   color - цвет заливки фигуры
        """
        self.k_cent = list(map(lambda  x, y: y - x, center, radius))
        self.center = (sum(x ** 2 for x in center)) ** 0.5
        self.radius = (sum(x ** 2 for x in (list(map(lambda  x, y: y - x, center, radius))))) ** 0.5
        if center_x is not None:
            self.cen_x = center_x
        if center_y is not None:
            self.cen_y = center_y
        if scale is not None:
            self.scale = scale
        if color is not None:
            self.color = color
    def square(self):
        """
        метод для нахождения площади окружности
        """
        self.square_circ = round(math.pi * self.radius ** 2, 3)
        return self.square_circ
    def perimeter(self):
        """
        метод для нахождения длины дуги окружности
        """
        self.length_circ = round(2 * math.pi * self.radius, 3)
        return self.length_circ
    def draw(self):
        """
        метод для построения заданной окружности
        """
        if hasattr(circ, 'cen_x') == True and hasattr(circ, 'cen_y') == True and hasattr(circ, 'scale') == True:
            if hasattr(circ, 'color'):
                canv.create_oval(self.cen_x - self.radius * self.scale, self.cen_y + self.radius * self.scale,
                                 self.cen_x + self.radius * self.scale, self.cen_x - self.radius * self.scale, fill = self.color)
            else:
                canv.create_oval(self.cen_x - self.radius * self.scale, self.cen_y + self.radius * self.scale,
                                 self.cen_x + self.radius * self.scale, self.cen_x - self.radius * self.scale)
        else:
            print('Для построения данной фигуры не хватает данных')
    def inform(self):
        """
        метод для вывода информации о данной окружности на экран
        """
        d = '\n'
        print(f'Информация о данной окружности {d}радиус: {self.radius} {d}длина окружности: {self.length_circ}{d}площадь: {self.square_circ}')


class Triangle(Figure):
    def __init__(self, a, b, c, center_x = None, center_y = None,scale = None, color = None, median = None, bisector = None, height = None):
        """
        конструктор экземпляра
        аргументы: a - координаты первой вершины треугольника
                   b - координаты второй вершины треугольника
                   c - координаты третьей вершины треугольника
                   center_x - центр оси абсцисс
                   center_y - центр оси ординат
                   scale - масштаб
                   median - медиана
                   bisector - биссектриса
                   height - высота
        """
        self.perimeter_tr = None
        self.a = a
        self.b = b
        self.c = c
        self.AB = list(map(lambda x, y: y - x, a, b))
        self.AC = list(map(lambda x, y: y - x, a, c))
        self.BC =list(map(lambda x, y: y - x, b, c))
        self.side_AB = round((sum(x ** 2 for x in list(map(lambda x, y: y - x, a, b)))) ** 0.5, 3)
        self.side_AC = round((sum(x ** 2 for x in list(map(lambda x, y: y - x, a, c)))) ** 0.5, 3)
        self.side_BC = round((sum(x ** 2 for x in list(map(lambda x, y: y - x, b, c)))) ** 0.5, 3)
        if center_x is not None:
            self.cen_x = center_x
        if center_y is not None:
            self.cen_y = center_y
        if scale is not None:
            self.scale = scale
        if color is not None:
            self.color = color
        if median is not None:
            self.median = median
        if bisector is not None:
            self.bisector = bisector
        if height is not None:
            self.height_tr = height

    def perimeter(self):
        """
        метод для нахождения периметра треугольника
        """
        self.perimeter_tr = round(self.side_AB + self.side_AB + self.side_BC, 3)
        return self.perimeter_tr
    def square(self):
        """
        метод для нахождения площади треугольника
        """
        p = (self.side_AB + self.side_AC + self.side_BC) / 2
        self.square = round(math.sqrt(p * (p - self.side_AB) * (p - self.side_AC) * (p - self.side_BC)), 3)
        return self.square
    def draw(self):
        """
        метод для построения заданного треугольника на координатной плоскости
        """
        d = '\n'
        if hasattr(trian, 'cen_x') == True and hasattr(trian, 'cen_y') == True and hasattr(trian, 'scale') == True:
            if hasattr(trian, 'color'):
                canv.create_polygon(self.cen_x + self.AB[0] * self.scale, self.cen_y - self.AB[1] * self.scale,
                                    self.cen_x + self.AC[0] * self.scale, self.cen_y - self.AC[1] * self.scale,
                                    self.cen_x + self.BC[0] * self.scale, self.cen_x - self.BC[1] * self.scale, fill = self.color, outline='black')
            else:
                canv.create_polygon(self.cen_x + self.AB[0] * self.scale, self.cen_y - self.AB[1] * self.scale,
                                    self.cen_x + self.AC[0] * self.scale, self.cen_y - self.AC[1] * self.scale,
                                    self.cen_x + self.BC[0] * self.scale, self.cen_x - self.BC[1] * self.scale, fill='', outline='black')
            canv.create_text(self.cen_x + self.AC[0] * self.scale - 12, self.cen_y - self.AC[1] * self.scale - 15, text = f'Triangle')
            canv.create_text(self.cen_x + self.AB[0] * self.scale, self.cen_y - self.AB[1] * self.scale + 6, text='A')
            canv.create_text(self.cen_x + self.AC[0] * self.scale + 6, self.cen_y - self.AC[1] * self.scale, text='C')
            canv.create_text(self.cen_x + self.BC[0] * self.scale, self.cen_y - self.BC[1] * self.scale + 6, text='B')
        else:
            print('Для построения данной фигуры не хватает данных')
    def inform(self):
        """
        метод для вывода информации о заданном треугольнике на экран
        """
        d = '\n'
        print(f'Информация о данном треугольнике {d}длина первой стороны а: {self.side_AB} {d}длина второй стороны b: {self.side_AC} {d}длина третьей стороны с: {self.side_BC} {d}периметр: {self.perimeter_tr} {d}площадь: {self.square}')


'''
2. Составить описание класса для вектора, заданного координатами его концов в трехмерном пространстве.
Реализовать операции сложения и вычитания векторов, результатом которого является вектор, а также
вычисления скалярного произведения двух векторов, длины вектора, косинуса угла между двумя векторами.
'''
class Vector():
    def __init__(self, koord_beg, koord_end, koord_beg1 = None, koord_end1 = None):
        """
        конструктор экземпляра
        Аргументы: koord_beg - координаты точки начала вектора
                   koord_end - координаты точки конца вектора
                   koord_beg1 - координаты точки начала второго вектора
                   koord_end1 - координаты точки конца второго вектора
        """
        self.lenn = None
        self.lenn_1 = None
        self.vect = list(map(lambda x, y: x - y, koord_end, koord_beg))
        if koord_beg1 is not None and koord_end1 is not None:
            self.vect_1 = list(map(lambda x, y: x - y, koord_end1, koord_beg1))
    def add(self):
        """
        сумма
        """
        if hasattr(vec, 'vect_1'):
            self.sum = list(map(lambda x, y: x + y, self.vect, self.vect_1))
            return self.sum
        else:
            print('Введите координаты второго вектора для нахождения суммы')
    def sub(self):
        """
        разность
        """
        if hasattr(vec, 'vect_1'):
            self.sub = list(map(lambda x, y: x - y, self.vect, self.vect_1))
            return self.sub
        else:
            print('Введите координаты второго вектора')
    def per(self):
        """
        метод для нахождения вектора произведения
        """
        if hasattr(vec, 'vect_1'):
            self.per = 0
            for i in range(len(self.vect)):
                if len(self.vect) == len(self.vect_1):
                    self.per += self.vect[i] * self.vect_1[i]
            return self.per
        else:
            print('Введите координаты второго вектора')
    def length(self):
        """
        метод для нахождения длины вектора
        """
        self.lenn = 0
        self.lenn_1 = 0
        for i in range(len(self.vect)):
            self.lenn += self.vect[i] ** 2
        if hasattr(vec, 'vect_1'):
            for i in range(len(self.vect_1)):
                self.lenn_1 += self.vect_1[i] ** 2
            return self.lenn and self.lenn_1
        else:
            return self.lenn
    def cos(self):
        """
        метод для нахождения косинуса угла между векторами
        """
        if hasattr(vec, 'vect_1'):
            self.cos = round(self.per / (self.lenn + self.lenn_1), 3)
            return self.cos
        else:
            print('Введите координаты второго вектора')

if __name__ == "__main__":
    cen_x = 500
    cen_y = 500
    canv = tk.Canvas(width = 1000, height = 1000, bg='white') # создание белого холста размером 1000*1000
    canv.pack()
    create_dpsk(1000, 1000, cen_x, cen_y, 30, 800, 800, 'black', 'black')
    width = (sum(x ** 2 for x in (list(map(lambda x, y: y - x, [10,20], [10, 50]))))) ** 0.5
    print(width)
    print((list(map(lambda x, y: y - x, [10,20], [30, 40]))))

    #1 задание

    rec = Rectangle([186,26], [300,100], cen_x, cen_y, 1)
    s_r = rec.square()
    p_r = rec.perimeter()
    rec.inform()
    rec.draw()


    print('- - -')


    circ = Circle([10,90],[50, 90], cen_x - 100, cen_y - 100, 1, 'pink')
    s_c = circ.square()
    p_c = circ.perimeter()
    circ.inform()
    circ.draw()


    print('- - -')


    trian = Triangle(a = [-7, 0], b = [1, 1], c = [3, 5], center_x = cen_x, center_y = cen_y, scale = 10, color = 'blue')
    s_t = trian.square()
    p_t = trian.perimeter()
    trian.inform()
    trian.draw()

    #2 задание
    vec = Vector([2,3,1], [7, 8, 6], [2,12,3], [4,0,15])
    s = vec.add()
    v = vec.sub()
    pr = vec.per()
    n = vec.length()
    c = vec.cos()
    print(f'длина заданного вектора: {n}')
    if hasattr(vec, 'vect_1'):
        print(f'Результирующий вектор суммы заданных векторов: {s}')
        print(f'Результирующий вектор разности заданных векторов: {v}')
        print(f'Результирующий вектор произведения заданных векторов: {pr}')
        print(f'длина двух заданных векторов: {n}')
        print(f'косинус угла между двумя заданными векторами: {c}')
tk.mainloop()










        
