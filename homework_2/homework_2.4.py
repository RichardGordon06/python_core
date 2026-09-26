number = 37
count = 1
trying = int(input('Мы загадали число, введите свой вариант: '))
while trying != number:
    count = count + 1
    if int(trying) > 37:
        print(trying, '> секретного числа')
    elif int(trying) < 37:
        print(trying, '< секретного числа')
    trying = int(input('Попробуйте ещё раз: '))
print('Ура! Вы отгадали число, это было число -', number)
print("Попыток затрачено", count)