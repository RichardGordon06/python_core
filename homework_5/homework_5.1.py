from functools import reduce

test_results = [
    {"name": "Test_Login", "status": "PASS", "duration": 1.5},
    {"name": "Test_Payment", "status": "FAIL", "duration": 3.2},
    {"name": "Test_Registration", "status": "PASS", "duration": 2.1},
    {"name": "Test_Cart_Update", "status": "SKIP", "duration": 0.1},
    {"name": "Test_Checkout", "status": "FAIL", "duration": 4.5},
    {"name": "Test_Logout", "status": "PASS", "duration": 0.8},
]

#  получаем все упавшие тесты (FAIL) с помощью filter()
failed_tests = list(filter(lambda test: test["status"] == "FAIL", test_results))

# формируем список названий упавших тестов с помощью map()
failed_titles = list(map(lambda test: test["name"], failed_tests))

# рассчитываем общее время выполнения всех тестов с помощью reduce()
# Передаем 0.0 в качестве начального значения (initializer), чтобы корректно суммировать duration
total_duration = reduce(lambda total, test: total + test["duration"], test_results, 0.0)

# формируем список названий успешно пройденных тестов (PASS)
passed_titles = [test["name"] for test in test_results if test["status"] == "PASS"]

# Подсчет количества тестов каждого статуса
pass_count = sum(1 for test in test_results if test["status"] == "PASS")
fail_count = sum(1 for test in test_results if test["status"] == "FAIL")
skip_count = sum(1 for test in test_results if test["status"] == "SKIP")

# Вывод результатов
print("--- Статистика автотестов ---")
print(f"Количество PASS: {pass_count}")
print(f"Количество FAIL: {fail_count}")
print(f"Количество SKIP: {skip_count}")
print(f"\nНазвания упавших тестов (FAIL): {failed_titles}")
print(f"Названия успешных тестов (PASS): {passed_titles}")
print("\nОбщее время выполнения всех тестов:", int(total_duration), "сек.")