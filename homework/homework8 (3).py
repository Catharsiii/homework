def factorial_f(k: int):
    '''
    фргументы: k - целое число
    Функция находит факториал числа k
    Возврат: число
    '''
    factor = 1
    for i in range(k):
        while k > 0:
            factor *= k
            k -= 1
    return factor   
#1. Написать функцию, которая принимает 2 аргумента. Если аргументы-числа, то возвращает их сумму. Если строки или списки, то возвращает конкатенацию.

def summa (arg_1: str or int or list or float, arg_2: str or int or list or float) :
    '''аргументы: arg_1, arg_2 - 2 элемента, принимающих любое значение
	   Если функция принимает числа, то возвращает их сумму
       Если функция принимает строки или списки, то в возвращает их конкатенацию
	   возврат: 	  
	'''
    sum == 0
    if type (arg_1) == float or type (arg_1) == int and type (arg_2) == float or type (arg_2) == int :
        arg_1 = arg_1 + arg_2   
    elif type (arg_1) == list and type (arg_2) == list :
        arg_1 = arg_1 + arg_2
    elif type (arg_1) == str and type (arg_2) == str :
        arg_1 = arg_1 + arg_2
    return arg_1
#print (summa ("1", "34"))

#2. Написать функцию, осуществляющую циклический сдвиг списка на указанное количество шагов и в указанном направлении.

def sdvig (number: int, x: int or float, spis: list) :
    '''
       аргументы: number - число, равное сдвигу списка.
	   Функция производит сдвиг заданного списка на указанное
       количество шагов ив указанном направлении
	   Возврат: список
	'''
    if x > 0 : #сдвиг вправо
        for i in range (len(spis),len(spis) - number, 1) :
            spis.insert (len(spis)-1)
        return spis
    elif x < 0 : #сдвиг влево
        for i in range (0, number, 1) :
            spis.append (spis.pop (0))
        return spis    
#print (sdvig (5, 1, [21, 34, 5, 245, 244, 23, 667, 467]))

#4. Написать функцию, вычисляющую число сочетаний .         
def combin(n: int, k: int):
    '''
       аргументы: n - целое число, k - целое число, причем n > k 
	   Функция находит число сочетаний из n по k
	   Возврат: число
	'''
    p = n - k
    factorial_1 = 1
    while n > 0 :
        factorial_1 *= n
        n -= 1
    factorial_2 = 1
    while p > 0 :
        factorial_2 *= p 
        p -= 1
    factorial_3 = 1 
    while k > 0 :
        factorial_3 *= k 
        k -= 1 
    result = factorial_1 / (factorial_2 * factorial_3)
    return result
#print (combin(n, k))	

#3. Написать функцию, вычисляющую число размещений без повторений .

def razm (n: int, k: int) :
    '''Аргументы: n, k - 2 целых числа, причем n > k.
	   Функция вычисляет число размещений без повторений из n по k
	   return: число	  
	'''
    return combin(n, k) * factorial_f(k)
#print (razm (10, 5))	   



#5. Написать программу, выводящую в консоль треугольник Паскаля.


def pascal(n: int):
    ''' 
        Создает треугольник Паскаля заданной высоты n
        Аргументы: n - высота треугольника
        Возврат: треугольник Паскаля
    '''
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    '''
        переписывает треугольник Паскаля в читаемом виде
        Аргументы: triangle - возврат функции pascal()
        Возврат: треугольник паскаля в читаемом виде
    '''
    for row in triangle:
        print(' '.join(map(str, row)).center(len(triangle[-1]) * 2))

triangle = pascal(6)
print_triangle(triangle)