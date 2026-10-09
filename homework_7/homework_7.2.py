class ATM:
    def __init__(self, twenty_count = 0, fifty_count = 0, hundred_count = 0):
        self.twenty_count = twenty_count
        self.fifty_count = fifty_count
        self.hundred_count = hundred_count

    def add_money(self, **kwargs):
        if not kwargs:
            "Вы не положили ни одной купюры."

        for banknote, count in kwargs.items():
            if banknote not in ['twenty', 'fifty', 'hundred']:
                raise ValueError (f"К сожалению, банкомат не принимает такие купюры: '{banknote}'")
            if count < 0:
                raise ValueError (f"Ошибка: количество купюр для '{banknote}' должно быть больше нуля.")

        for key, value in kwargs.items():
            if key == 'twenty':
                self.twenty_count += value
            elif key == 'fifty':
                self.fifty_count += value
            elif key == 'hundred':
                self.hundred_count += value

    def withdraw(self, amount): #Снятие средств
        sum_20 = self.twenty_count *  20
        sum_50 = self.fifty_count * 50
        sum_100 = self.hundred_count * 100
        if amount > (sum_20 + sum_50 + sum_100):
            raise ValueError('Недостаточно средств')
        if amount % 10 != 0 or amount == 10 or amount == 30:
            raise ValueError('Банкомат не может выдать такую сумму имеющимися купюрами')

        remains = amount

        # Высчитываем 100-рублевые купюры
        take_100 = min(remains // 100, self.hundred_count)
        remains -= take_100 * 100  # Уменьшаем остаток запрашиваемой суммы

        # Высчитываем 50-рублевые купюры
        take_50 = min(remains // 50, self.fifty_count)
        remains -= take_50 * 50

        # Высчитываем 20-рублевые купюры
        take_20 = min(remains // 20, self.twenty_count)
        remains -= take_20 * 20

        # Корректировка для сложных случаев (например, нужно выдать 60р, соток нет, код взял одну 50р, остался остаток 10р.
        if remains != 0 and take_50 > 0 and (remains + 50) <= (self.twenty_count - take_20) * 20:
            remains += 50
            take_50 -= 1
            additional_20 = remains // 20
            take_20 += additional_20
            remains -= additional_20 * 20

        # Если после всех разменов сумма не обнулилась, значит набрать её текущими купюрами невозможно
        if remains != 0:
            raise ValueError('Невозможно набрать точную сумму имеющимися купюрами')

        # Уменьшаем остаток купюр в банкомате
        self.hundred_count -= take_100
        self.fifty_count -= take_50
        self.twenty_count -= take_20

        print(f'Успешно выдано: 100р x {take_100}, 50р x {take_50}, 20р x {take_20}. Всего: {amount} руб.')
        return True

    def show_money(self):
        return self.twenty_count, self.fifty_count, self.hundred_count


one = ATM(10, 10, 10)
two = one.add_money(twenty = 2, fifty = 5, hundred = 11)
three = one.withdraw(60)
four = one.withdraw(1560)

print(one.show_money())


