import sys
#2.	Напишите программу, которая принимает несколько чисел и операцию через sys.argv, выполняет операцию над введенными числами и выводит результат.
#        Если аргументы не переданы, выведите сообщение об ошибке.
def operation():
    '''
    Функция ничего не принимает
    
    '''
    spis = sys.argv[1:]
    if len(spis) > 3:
        if '*' in spis:
            ind = spis.index('*')
            spis.pop(ind)
            oper = 1    
            for el in spis:
                oper *= int(el)
        if '+' in spis:
            ind = spis.index('+')
            spis.pop(ind)
            oper = 0    
            for el in spis:
                oper += int(el)
        if '-' in spis:
            ind = spis.index('-')
            spis.pop(ind)
            oper = int(spis[0])    
            for i in range(1, len(spis)):
                oper -= int(spis[i])
        if '\\' in spis:
            ind = spis.index('\\')
            spis.pop(ind)
            oper = int(spis[0])    
            for i in range(1, len(spis)):
                oper /= int(spis[i])
        print(spis)
    


#3.	Реализуйте программу, которая проверяет,
#       работает ли она на операционной системе Windows. Если да, то выводит соответствующее сообщение. 
def check():
    '''
    Функция не принимает никакие аргументы
    Функция проверяет, работает ли она на операционноqй системе Windows
    Вывод: если скрипт выполняется на Windows - "Программа работает на Windows"
           иначе - "Программа работает не на Windows"
    '''
    if "win" in sys.platform:
        print("Программа работает на Windows")
    else:
        print("Программа работает не на Windows")
#4.	Напишите программу, которая ограничивает глубину рекурсии до 500 и вызывает
#       рекурсивную функцию, пока не достигнет лимита. 
def rec(n: int):
    '''
    аргументы: n - число, факториал которого нужно найти
    Рекурсивная функция. Находит факториал заданного числа
    возрат: число - факториал n
    '''
    if n == 1:
        return n
    else:
        return n * rec(n - 1)
def func():
    '''
    аргументы: пусто
    вызывает рекурсивную функцию до того момента, пока она не достигнет лимита
    возрат: число - факториал n
    '''
    sys.setrecursionlimit(500)
    k = sys.getrecursionlimit()
    return(rec(k - 3))

if __name__ == "__main__":
    #check()
    #print(func())
    print(operation())