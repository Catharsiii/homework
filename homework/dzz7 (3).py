def minimum(x, y):
	'''
	   Аргументы: x, y - 2 числа с плавающей точкой.
	   Находит минимальное число из двух полученных.
	   Возврат: минимальное число	  
	'''
	if x > y:
		return y
	else:
		return x
#print ("Минимальное число: "minimum(2,2))
#2.	Написать функцию, для поиска максимума трёх чисел.
def maxi(x: int or float, y: int or float, z: int or float):
	'''
	  arguments: x, y, z - 3 числа типа данных с плавающей точкой .
	  Находит минимальное число из трех полученных
	  return: возвращает число типа запятой с плавающей точкой,
	          которое является мксимальным из трех полученных.
	'''
	maxi = 0
	if  x > y and x > z :
		maxi = x	
	elif x == y or x == z:
			maxi = x
	elif y > x and y > z :
		maxi = y
		if y == x or y == z:
			maxi = y
	else:
		maxi = z
	return maxi
#print("Максимальное число: ", maxi(45,45, 9))
#3.	Написать функцию для суммирования чисел списка.
def summa(spis: list):
	'''arguments: spis - список с элементами числами типа данных с плавающей точкой
	   Суммирует все элементы списка
	   return: сумма всех чисел
	'''
	sum = 0
	for i in spis :
		sum += i
	return sum
#print ('сумма всех чисел списка:',summa([202.45, 343.25, 225.3]))
#4.	Написать функцию для перемножения чисел списка.
def multip(spis: list):
	'''arguments: spis - список с элементами числами типа данных с плавающей точкой.
	   Перемножает все элементы списка.
	   return: число - произведение всех элементов списка.
	'''
	pr = 1
	for i in spis :
		pr *= i
	return pr
#print("Произведение всех элементов списка: ", multip([20,2,12]))
#5.	Написать функцию для обращения строки.
def reverse_str (stroka: str) :
    '''
    arguments: stroka - строка
    Переворачивает строку
	return: строка
	'''
    str_new = ''
    for i in range (len (stroka)-1, -1, -1) :
        str_new += stroka[i]
    return str_new
#print ("Перевернутая строка: ",reverse_str ('stroka_for_reversing'))		
#6.	Написать функцию для вычисления факториала числа. Функция принимает число в качестве аргумента.
def fakt(number: int) :
	'''arguments: number - целое число.
	   Находит факториал числа
	   return: число
	'''
	factorial = 1
	while number> 1:
		factorial *= number
		number -= 1
	return factorial
#print("Факториал числа: ", fakt(5))	 
#7.	Написать функцию проверки, находится ли число в заданном диапазоне.
def proverka (number: int, start: int, end: int) :
	'''
		arguments: number - проверяемое число
				   start, end - начало и конец диапазона
		Проверяет, находится ли число в диапазоне
		return: True - если число в диапазоне, False - если число не в диапазоне
	'''
	return start < number < end
#print(proverka (3, 2, 566))	
#8.	Написать функцию, которая суммирует все целые числа в указанном диапазоне от start до end. Если start больше чем end, то поменять их местами.
def summa (start: int or float, end: int or float) :
    '''arguments: start,  end - числа с плавающей точкой.
	   Суммирует все целе числа в указанном диапазоне. Если start > end, меняет их местами
	   return: число
	'''
    sum = 0
    if start < end :
        for i in range (start, end + 1) :
            sum += i
    elif start > end :
        for i in range (end, start + 1) :
            sum += i
    return sum
print (summa (10,15))
