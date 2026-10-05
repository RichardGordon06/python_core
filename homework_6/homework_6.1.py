def calculate(spisok):
    if not spisok:
        return 0
    elif spisok[0] == 'PASS':
        return 1 + calculate(spisok[1:])
    else:
        return calculate(spisok[1:])

tests_list = ['PASS', 'SKIP', 'FAIL', 'PASS', 'PASS']

print(calculate(tests_list))