with open('numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split())) #код по примеру предыдущего задания
    for i in numbers: #Перебираем числа, и проверяем на чёт и нечет и сразу записываем в файл
        if i % 2 == 0:
            with open('chet.txt', 'a') as file:
                file.write(str(i) + '\n')
        else:
            with open('nechet.txt', 'a') as file:
                file.write(str(i) + '\n')