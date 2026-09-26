for i in range(1,31):
    if i % 5 == 0 and i % 3 == 0: #Проверка возможности деления И на 3 И на 5
        print('BugTest')
    elif i % 3 == 0:  # Проверка деления на цело для 3х
        print('Bug')
    elif i % 5 == 0:  # Проверка деления на цело для 5ти
        print('Test')
    else:
        print(i)