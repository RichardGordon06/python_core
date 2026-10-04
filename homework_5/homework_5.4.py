class InvalidTestStatusError(Exception):
     #Исключение, вызываемое при указании некорректного статуса теста
    pass

correct_statuses = ["PASS", "FAIL", "SKIP"] #Корректные статусы

def test_status():
    data = input('Пожалуйста, напишите статус теста: ') #Ввод данных
    status = data.upper()
    if status not in correct_statuses: #Проверка данных и вывод ошибки
        print(f'{data} некорректный статус')
        raise InvalidTestStatusError
    else:
        print("Корректный статус")

try: #Обёртка для отлова ошибок
    test_status()
except InvalidTestStatusError as e:
    print(f"Необходимо ввести один из трёх вариантов: FAIL, PASS, SKIP."
          f"\nПопробуйте снова")