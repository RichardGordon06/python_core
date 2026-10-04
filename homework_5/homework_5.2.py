import json

file_name = "test_users.json"
required_fields = ["login", "password", "expected_result"]

try:
    # Открываем и загружаем JSON-файл
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict) or "test_users" not in data:
        raise ValueError("Некорректная структура JSON: отсутствует корневой ключ 'test_users'")

    # Итерируемся по списку пользователей
    for index, user in enumerate(data["test_users"], start=1):
        try:
            print(f"Проверка пользователя №{index}:")

            # Проверяем наличие всех обязательных полей
            for field in required_fields:
                if field not in user:
                    # Генерируем ошибку KeyError вручную, чтобы перехватить её в блоке except
                    raise KeyError(field)

            # Если все поля на месте, выводим информацию
            print(f"  Логин: {user['login']}")
            print(f"  Пароль: {user['password']}")
            print(f"  Ожидаемый результат: {user['expected_result']}\n")

        except KeyError as e:
            print(f"Ошибка данных: У пользователя №{index} отсутствует обязательное поле {e}\n")

# Обработка ошибки: файл не найден
except FileNotFoundError as e:
    print(f"Критическая ошибка: Файл '{file_name}' не существует. Подробности: {e}")

# Обработка ошибки: файл не является валидным JSON
except json.JSONDecodeError as e:
    print(f"Критическая ошибка: Невозможно прочитать содержимое как JSON. Подробности: {e}")

# Обработка других возможных ошибок (например, неверная структура корневого элемента)
except ValueError as e:
    print(f"Критическая ошибка валидации: {e}")

# Обработка непредвиденных системных ошибок
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")