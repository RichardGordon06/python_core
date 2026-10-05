from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Перед вызовом функции её данные:')
        print('Название функции:', func.__name__)
        print(f'Её аргументы {args}')
        print(f'Именованные аргументы {kwargs}')
        retuslt = func(*args, **kwargs)
        print(f'Функция [{func.__name__}] завершена')
        return retuslt
    return wrapper

@log_test
def calculate(x, y, z = 0):
    sum = x + y + z
    show_sum = print(f'Итоговый результат: {sum}')
    return show_sum

calculate(1, 2, z=5)
