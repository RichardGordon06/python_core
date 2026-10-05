def create_time_checker(max_time):
    def time_checker(x):
        if x > max_time:
            return f'Превышен Лимит 1: {x} > {max_time}'
        elif x < max_time:
            return f'Превышен лимит 2: {x} < {max_time}'
        else:
            return f'Вы ввели какую-то чушь {x} не подходит ни под одно из условий, попробуйте снова'
    return time_checker

time_5 = create_time_checker(5)
time_10 = create_time_checker(10)

print(time_5(50))
print(time_5(5))
print(time_10(2))
