with open('numbers.txt', 'r') as file: #Читаем файл
    numbers = list(map(int, file.read().split())) #Разбираем числа отдельно, и помещаем в список для удобства
    count_items = len(numbers) #Считаем количество чисел
    if count_items < 3:
        print('Ошибка, чисел в файле должно быть больше 3х')
    else:
        print(numbers[0], numbers[1], numbers[count_items - 2], numbers[count_items - 1]) #Выводим искомое