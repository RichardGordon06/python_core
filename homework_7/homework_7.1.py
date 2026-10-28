class CreditCard:
    def __init__(self, number, balance):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть меньше 0")
        self.number = number
        self.__balance = balance

    def show_info(self): #Баланс
        return f'Номер карты: {self.number}, баланс: {self.__balance}'

    def deposit(self, amount): #Пополнение
        if amount <= 0:
            raise ValueError('Сумма пополнения не может быть меньше 0')
        self.__balance += amount

    def withdraw(self, amount): #Снятие средств
        if amount <= 0:
            raise ValueError('Сумма должна быть больше 0')
        if amount > self.__balance:
            raise ValueError('Недостаточно средств')
        self.__balance -= amount

card_1 = CreditCard(123, 100) #Задаём начальный баланс карт
card_2 = CreditCard(321, 2000)
card_3 = CreditCard(2315, 500)

card_1.deposit(150) #Пополнение 1 карты
card_2.deposit(500) #Пополнение 2 карты
card_3.withdraw(150) #Снятие с 3 карты


print(card_1.show_info())
print(card_2.show_info())
print(card_3.show_info())