'''1. Создать класс с двумя переменными. Добавить метод вывода на экран и метод изменения этих переменных.
   Добавить метод, который находит сумму значений этих переменных, и метод который находит наибольшее
   значение из этих двух переменных.'''
class Work_w_num:
    def __init__(self, a, b):
        """
        Конструктор экземпляра
        аргументы: self - ссылка на экземпляр
                   a - первый атрибут экземпляра
                   b - второй атрибут экземпляра
        """
        self.a = a
        self.b = b
    def display(self):
        """
            Метод для вывода значений атрибутов на экран
            аргументы: self - ссылка на экземпляр
            вывод: значения атрибутов
        """
        print(f'Значение a: {self.a}, Значение b: {self.b}')
    def change_n(self, new_a, new_b):
        """
            Метод для изменения значений переменных a и b
            аргументы: self - ссылка на экземпляр
                       new_a - переменная, содержащая новое значение атрибута a
                       new_b - переменная, содержащая новое значение атрибута b
        """
        self.a = new_a
        self.b = new_b
    def sum_n(self):
        """
            Метод для нахождения суммы атрибутов
            аргументы: self - ссылка на экземпляр
            возврат: сумма атрибутов
        """
        return self.a + self.b
    def max_n(self):
        """
            метод для нахождения наибольшего атрибута
            аргументы: self - ссылка на экземпляр
            возврат: наибольший из атрибутов
        """
        return max(self.a, self.b)

'''2. Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне.
   Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
   Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. Написать программу,
   демонстрирующую все возможности класса.'''


class Counter:
    def __init__(self, min_n = 0, max_n = 5, cur_n = 0):
        """
        конструктор объекта класса
        аргументы: min_n - минимальное число заданного диапазона
                   max_n - максималньое значение данного диапазона
                   cur_n - текущее значение
        """
        self.min_n = min_n
        self.max_n = max_n
        self.cur_n = cur_n
        if cur_n < min_n or cur_n > max_n:
            print(f'Текущеее число должно быть в заданном диапазоне от {min_n} до {max_n}')
    def increaser(self):
        """
            метод для увеличения значения атрибута на 1 на заданном диапазоне
            аргументы: self - ссылка на экземпляр
        """
        if self.cur_n < self.max_n:
            self.cur_n += 1
        else:
            print(f'Текущеее число должно быть в заданном диапазоне от {self.min_n} до {self.max_n}')
    def decrease(self):
        """
            метод для уменьшения значения атрибута на 1 на заданном диапазоне
            аргументы: self - ссылка на экземпляр
            возврат: наибольший из атрибутов
        """
        if self.cur_n > self.min_n:
            self.cur_n -= 1
        else:
            print(f'Текущеее число должно быть в заданном диапазоне от {self.min_n} до {self.max_n}')

'''
    3. Составить описание класса многочленов от одной переменной, задаваемых сте¬пенью многочлена и массивом коэффициентов.
 Предусмотреть методы для вы¬числения значения многочлена для заданного аргумента, операции сложения,
 вычитания и умножения многочленов с получением нового объекта-многочлена.
'''

class Mnog:
    def __init__(self, koef_value, x, koef_value1 = None, y = None):
        """
            Конструктор экземпляра
            аргументы: self - ссылка на экзепляр
                       koef.value - набор коэффицциентов многочлена
                       x - переменная многочлена
                       koef.value1 - набор коэффициентов 2-го многочлена
                       y - переменная второго многочлена
        """
        self.mn = koef_value
        self.deg = (len(koef_value) - 1)
        self.per = x
        self.mn1 = koef_value1
        self.deg1 = (len(koef_value1) - 1)
        self.per1 = y
    def calc(self):
        """
            Метод для нахождения суммы многочленов
            аргументы: self - ссылка на экземпляр
            возврат: сумма атрибутов
        """
        cur_x = 0
        for i in reversed(self.mn):
            cur_x += i * self.per ** self.deg
            self.deg -= 1
        return cur_x
    def sum_mn(self):
        """
            Метод для нахождения суммы атрибутов
            аргументы: self - ссылка на экземпляр
            возврат: писок коэффициентов нового многочлена
        """
        new_mn = []
        if self.deg == self.deg1:
            new_mn = list(map(lambda x, y: x + y, self.mn, self.mn1))
        else:
            max_deg = max(self.deg, self.deg1)
            self.mn = self.mn + [0] * (max_deg - self.deg)
            self.mn1 = self.mn1 + [0] * (max_deg - self.deg1)
            new_mn = list(map(lambda x, y: x + y, self.mn, self.mn1))
        return new_mn
    def subt_mn(self):
        """
            Метод для нахождения разности атрибутов
            аргументы: self - ссылка на экземпляр
            возврат: список коэффициентов нового многочлена
        """
        new_mn = []
        if self.deg == self.deg1:
            new_mn = list(map(lambda x, y: x - y, self.mn, self.mn1))
        else:
            max_deg = max(self.deg, self.deg1)
            self.mn = self.mn + [0] * (max_deg - self.deg)
            self.mn1 = self.mn1 + [0] * (max_deg - self.deg1)
            new_mn = list(map(lambda x, y: x - y, self.mn, self.mn1))
        return new_mn
    def mult_mn(self):
        """
            Метод для нахождения произведения многочленов
            аргументы: self - ссылка на экземпляр
            возврат: список коэффициентов нового многочлена
        """
        new_mn = []
        for i in range(self.deg1+1):
            for j in range(self.deg+1):
                new_mn.append(self.mn[j] * self.mn1[i])
        return new_mn


if __name__ == "__main__":
    '''
    # 2-e задание
    cl = Counter(0, 5)
    i = 0
    while i < 6:
        
        cl.increaser()
        i += 1
    # 1-e задание

    opr = Work_w_num(10, 20)
    opr.display()
    print(opr.sum_n())
    print(opr.max_n())
    opr.change_n(45, 15)
    opr.display()
    print(opr.sum_n())
    print(opr.max_n())
    '''
    # 3-d task

    mn = Mnog([23, 2, 5, 7], 3, [1, 2, 3, 4, 5, 1])
    print(mn.calc()) # УРАААААААААААААААААААААААААААА
    print(mn.sum_mn())
    print(mn.subt_mn())
    print(mn.mult_mn())
