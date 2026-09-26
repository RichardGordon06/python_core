import test_data

def main():
    count_active = 0
    count_blocked = 0
    count_inactive = 0
    count_data = input('Введите количество тестовых пользователей: ')
    count = int(count_data)
    users = [test_data.generate_user() for i in range(count)]
    for user in users:
        if user['status'] == 'ACTIVE':
            print(user)
            count_active += 1
        elif user['status'] == 'BLOCKED':
            print(user)
            count_blocked += 1
        elif user['status'] == 'INACTIVE':
            print(user)
            count_inactive += 1
    print('Из них в статусе ACTIVE:', count_active)
    print('Из них в статусе BLOCKED:', count_blocked)
    print('Из них в статусе INACTIVE:', count_inactive)
    return users

main()