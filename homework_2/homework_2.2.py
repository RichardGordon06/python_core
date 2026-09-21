cont_try = 2 #задаём число попыток не считая первую
password = input('Введите пароль: ')
while password != 'Python123' and cont_try != 0:
    cont_try -= 1
    print('Введённый пароль неправильный, пропробуйте снова (попыток',  cont_try + 1,')')
    password = input('Попробуйте ещё раз: ')
    if cont_try == 0 and password != 'Python123':
        print('Доступ запрещён, слишком много попыток входа')
    else:
        if password == 'Python123':
            print('Пароль Успешен')
        else:
            continue