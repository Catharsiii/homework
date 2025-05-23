#1.	Дано натуральное число. Вычислите сумму его цифр.
#def sum (num: int):
def summ(n: int):
    '''
    Аргументы: функция принимает натуральное число n
    Находит сумму цифр, из которых состоит число
    Возврат: Если передана цифра - возвращает эту цифру
             Если передано число - возвращает сумму его цифр
             Если n = 0 или n < 0 - возвращает строку 'Функция принимает только натуральные числа'

    '''
    if n > 9:
        return int(n % 10) + summ(n // 10)
    if 0 < n < 10:
        return n
    else:
        return 'Функция принимает только натуральные числа'

#2.	Дано натуральное число. Записать число в обратном порядке
def reversion(k: int):
    '''
    Аргументы: функция принимает натуральное число n
    Переворачивает это натуральное число
    Возврат: число в обратном порядке

    '''
    if int(k) > 9:
        ost = int(k) % 10
        k = str(k)
        return str(ost) + str(reversion(k[0:len(k) - 1]))   
    if 0 < int(k) < 10:
        return k  
    else:
        'Функция принимает только натуральные числа'    

#3.	Проверить число на простоту
def check(n, delit = 2):
    '''
    Аргументы: функция принимает натуральное число n
    Проверяет число на простоту
    Возврат: Если n - простое число - True
             Если n - простое число - False
             Если n = 0 или n = 1 - возвращает строку 'Цифры 0 и 1 не являются ни простыми, ни сложными числами' 
    '''
    if n == delit:
        return True
    elif n == 0 or n == 1:
        return 'Цифры 0 и 1 не являются ни простыми, ни сложными числами'    
    elif n % delit == 0:
        return False
    return check(n, delit + 1)

#4.	Написать функцию, которая будет принимать натуральное число n и возвращать n-ую строку треугольника Паскаля.
def pascal_str(n):
    '''
    Функция создает n- строку треугольниука Паскаля
    Аргументы: n - номер строки треугольника Паскаля
    Возврат: n - я строка Паскаля
    '''
    return [int(binom.combin(n, k)) for i in range(n + 1)]

#5.	Написать функцию генерации перестановок из заданного массива заданной длины

def Perm(lst,n):
    if n<=0:
        return 'Перестановок нет'
    k = 0
    l=[]
    for i in range(0, len(lst)): 
        m=lst[i] # текущий эл
        remLst=lst[:i] + lst[i+1:] #remLst = список, в который с помощью цикла мы закидываем все элементы изначальной последовательности чисел.
        #print(remLst)
        for p in Perm(remLst,n-1): 
            print(remLst)
            l.append([m]+p) 
            k += 1
            print(k)
            print(p, m)
    return l 

'''def prov(n:int or float):
    k = 0
    delit = [2, 3, 5, 7]
    for i in delit:
        if n % delit[i] != 0:
            k += 1
        else:
            continue
    return prov(n - 1) #f n != 0 and n != 1 else 'Число не является ни простым, ни сложным'
print(prov(45))'''
"""
if num > 1:
   for i in range(2,num):
      if (num % i) == 0:
         print(num,"is not a prime number")
         print(i,"times",num//i,"is",num)
         break
   else:
      print(num,"is a prime number")

else:
   print(num,"is not a prime number")"""

'''def prov(n:int or float):
    k = 0
    if n != 0 and n != 1:
        if n % 2 == 0:
            k += 1
        if n % 3 == 0:
            k += 1
        if n % 5 == 0:
            k += 1
        if n % 7 == 0:
            k += 1
    else:
        return 1
    return prov(n - 1) #f n != 0 and n != 1 else 'Число не является ни простым, ни сложным'
print(prov(45))'''
if __name__ == "__main__":
    #print(summ(45767))
    #print(reversion('123456'), sep = '')
    print(check(117))
    #print(Perm([1, 23, 6, 46],3))
