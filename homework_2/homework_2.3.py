for i in range(1, 21):
    if i % 5 == 0:
        print('Тест пропущен')
        pass
    elif i == 18:
        print('Завершение тестирования')
        break
    else:
        print(i)