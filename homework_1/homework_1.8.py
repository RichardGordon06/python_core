second_stroka = input("\nВведине строку, в которой будет производится поиск: ")
first_stroka = input("\nВведине строку, которую нужно найти в первой: ")
if first_stroka in second_stroka:
    print('Да, строка', first_stroka, 'действительно находится в', second_stroka, '\n')
else: print('Попробуйте снова в следующий раз:)', '\n')