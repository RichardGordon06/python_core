with open('veshestven.txt', 'r') as file:
    numbers = list(map(float, file.read().split()))
    with open('veshestven.txt', 'w'):
        for i in numbers: #Берём числа по одному, возводим в квадрат и записываем в конец
            with open('veshestven.txt', 'a') as file:
                num = i ** 2
                file.write(str(num) + '\n')