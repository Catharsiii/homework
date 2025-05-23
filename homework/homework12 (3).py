import os
#1. Написать функцию, которая выводит список файлов заданного каталога, с указанием размеров файлов и даты их последней модификации
def finder(path: str):
    """
        Функция принимает переменну path - абсолютный путь к каталогу,
              список файлов которго нужно вывести
        для каждого файла из этой директории находит его название,
              дату его последнего изменения и размер
        возврат: список
        
    """
    import os, time, datetime
    listt = []
    os.chdir(path)
    for el in os.listdir(path):        
        time_last_ch = datetime.datetime.strptime(time.ctime(os.path.getmtime(fr"{path}/{el}")),"%a %b %d %H:%M:%S %Y")
        size = os.path.getsize(fr"{path}/{el}")
        if os.path.isdir(el):
            listt.append(el + ' ' + str(time_last_ch) + ' ' + 'folder')
        else:
            listt.append(el + ' ' + str(time_last_ch) + ' ' + str(size) + " Bytes")
    return(listt)
            

#2.	Написать функцию, которая создает резервную копию заданного файла/каталога в имени резервной копии должны использоваться дата и время создания резервной копии
def copy_create(begin: str, end: str = None):
    '''
        функция создает резервную копию заданного файла/каталога
        На вход функция принимает 2 параметра: begin, end
            begin: абсолютный путь до копируемого файла/каталога
            end(необязательный параметр): абсолютный путь до директории, в которую копируется файл/каталог
                Если end пусто, функция сохраняет резервную копию в папку, где находится файл/каталог для копирования
                Если end не пусто, функция сохраняет резервную копию по указанному пути  
        Возврат: пусто   
    '''
    import shutil, datetime
    time_copy = str(datetime.datetime.now().strftime('%Y.%m.%d %H.%M.%S'))
    if end is None:
        shutil.copytree(begin, fr"{begin} (Резервная копия {time_copy})")
    else: 
        shutil.copytree(begin, fr"{end}/{begin.split('\\')[-1]} (Резервная копия {time_copy})")

#3.	Написать Функцию, которая рисует дерево каталогов заданного каталога

def dir_tree(directory: str, ind = 0):
    '''
        Функция создает дерево каталогов заданной директории
        аргументы: directory - директория для создания дерева
        Возврат: пусто
    '''
    
    elements = os.listdir(directory)
    for i, el in enumerate(elements):
        path = os.path.join(directory, el)
        print(' ' * ind + '├── ' + el)
        if os.path.isdir(path) == True:
            dir_tree(path, ind + 4)

#4. Написать аналог команды cat (OS Linux)
def cat(path1: str = None, operation: str = None):
    '''
    Функция читает данные из стандартного ввода и выводит их содержимое в стандартный вывод
    аргументы: path1 - абсолютный путь к файлу
               operation - переменная, от значения которой зависят действия функции:
                           n - нумерация всех строк файла
                           b - нумерация только непустых строк
                           = None - вывод файла без пустых строк
    Возврат: список с полученными и обработанными файлами
    '''
    spis = []
    if operation == "n" and path1 is not None:
        with open(path1, 'r') as f:
            k = 0
            for line in f.readlines():
                k += 1
                r = str(k) + '. ' + line
                spis.append(r.strip())
        return spis
    if operation == "b" and path1 is not None:
        with open(path1, 'r') as f:
            k = 0
            for line in f.readlines():
                if len(line.strip()) == 0:
                    continue
                else:
                    k += 1
                    r = str(k) + '. ' + line
                    spis.append(r.strip())
            return spis
    if operation == None and path1 is not None:
        with open(path1, 'r') as f:
            for line in f.readlines():
                if len(line.strip()) == 0:
                    continue
                spis.append(line.strip())
            return spis




if __name__ == '__main__':
    #print(*finder(r"C:\Users\1\Documents\ДЗ\ДЗ"), sep='\n')
    #aaa(r"C:\Users\1\Documents\ДЗ\ДЗ")
    #dir_tree(r"C:\Users\1\Documents\ДЗ")
    print(*cat(r"C:\Users\1\Downloads\Задача на вектора (3).docx", "b"), sep = '\n')