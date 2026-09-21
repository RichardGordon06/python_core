for i in range(1,31):
    if i % 3 == 0:  # Проверка деления на цело для 3х
        print('Bug')
    elif i % 5 == 0:  # Проверка деления на цело для 5ти
        print('Test')
    else:
        print(i)