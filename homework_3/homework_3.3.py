import random

tests = [ "test_login",
          "test_logout",
          "test_registration",
          "test_profile",
          "test_payment",
          "test_search" ]

tests_count = len(tests)

statuses = ["PASS", "FAIL", "SKIP"]

numbers_tests = input('Введите количество необходимых тестов: ')
count_tests = int(numbers_tests)

if int(count_tests) > int(tests_count):
    print('Количество тестов, превышает количество доступных тест-кейсов')
elif int(count_tests) <= 0:
        print("Ошибка: Количество тестов должно быть больше нуля.")
else:
    selected_tests = random.sample(tests, count_tests)
    for test in selected_tests:
        random_status = random.choice(statuses)
        print(f"{test}: {random_status}")
