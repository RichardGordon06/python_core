count_pass = 0
count_fail = 0
count_skip = 0
print('Здравствуйте, ниже, нужно будет ввести результаты автотестов, допустимые значения только FAILL, PASS, SKIP')
test_result = input("Пожалуйста, введите результаты автотестов одной строй, через пробел: ").upper()
tests = test_result.split()
total_tests = len(tests)
for test in tests:
    if test == 'PASS': #Проверяем введённый результат на PASS и считаем количество
        count_pass += 1
    elif test == "FAIL": #Проверяем введённый результат на FAIL и считаем количество
        count_fail += 1
    elif test == "SKIP": #Проверяем введённый результат на SKIP и считаем количество
        count_skip += 1

print('Всего тестов:', total_tests)
print('PASS:', count_pass)
print('FAIL:', count_fail)
print('SKIP:', count_skip)
percent_pass = count_pass / total_tests * 100
print('Успешно:', int(percent_pass), end = '%')
