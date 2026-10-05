from functools import wraps

def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                print(f"Попытка {i + 1} из {count}")
                func(*args, **kwargs)

            print(f"{count} попыток исчерпано. Возвращаем True")
            return True
        return wrapper
    return decorator

@retry(10)
def func ():
    print('Функция для повтора')
    return False

final_status = func()
print(f"Что вернул декоратор наружу: {final_status}")

