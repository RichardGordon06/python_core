class Flower:
    def __init__(self, name, price, life_time):
        if price <= 0:
            raise ValueError (f'Ошибка: Цена цветка не может быть = 0')
        self.name = name
        self.price = price
        self.life_time = life_time

class Accessory:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError('Ошибка: Цена аксессуара не может быть отрицательной')
        self.name = name
        self.price = price

# Букет, содержащий цветы
class Bouquet:
    def __init__(self):
        self.flowers = {}
        self.accessories = []

    #Добавление цветов
    def add_flower(self, flower, count=1):
        if count <= 0:
            raise ValueError (f'Ошибка: Количество цветов не может быть отрицательным, или равным 0')
        if flower in self.flowers:
            self.flowers[flower] += count  # Если такой цветок уже есть, увеличиваем количество
        else:
            self.flowers[flower] = count  # Если нет, добавляем новую запись

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

# Для проверки наличия цветка
    def has_flower(self, flower_name):
        if isinstance(flower_name, Flower):
            name = flower_name.name
        else:
            name = flower_name
        lower = name.lower()
        for flower in self.flowers.keys():
            if flower.name.lower() == lower:
                print(f'Да, такой цветок есть в букете')
                return True
        print(f'К сожалению, такого цветка нет в букете')
        return False

#подсчёт цены
    def total_price(self):
        total = 0
        # Перебираем словарь: flower — объект цветка, cnt — его количество
        for flower, cnt in self.flowers.items():
            total += flower.price * cnt

        for acc in self.accessories:
            total += acc.price
        return total

# Сортировка по цене
    def show_sorted_by_price(self, sort = 'ASC'):
        if sort == "ASC":
            print("\n Сортировка по цене (от дешёвых к дорогим)")
            sorted_flowers = sorted(self.flowers.keys(), key=lambda flower: flower.price)
            for flower in sorted_flowers:
                cnt = self.flowers[flower]  # Достаем количество этого цветка из словаря
                print(f" - {flower.name}: {cnt} шт. (Цена: {flower.price} руб./шт.)")
        elif sort == "DESC":
            print("\n Сортировка по цене (от дорогих к дешёвым)")
            sorted_flowers = sorted(self.flowers.keys(), key=lambda flower: flower.price, reverse=True)
            for flower in sorted_flowers:
                cnt = self.flowers[flower]  # Достаем количество этого цветка из словаря
                print(f" - {flower.name}: {cnt} шт. (Цена: {flower.price} руб./шт.)")
        else:
            raise ValueError (f'{sort} Такая сортировка не поддерживается, введите либо ASC, либо DESC')

#Среднее время жизни букета
    def get_life_time(self):
        total_life_time = 0
        total_count = 0
        for flower, cnt in self.flowers.items():
            total_life_time += flower.life_time * cnt
            total_count += cnt
        if total_count == 0:
            return 0
        return total_life_time / total_count

    def show_bouquet(self):
        print("\n Букет")
        for flower, cnt in self.flowers.items():
            print(f" - {flower.name}: {cnt} шт. (по {flower.price} руб./шт.)")
        if self.accessories:
            print("Аксессуары:")
            for acc in self.accessories:
                print(f" - {acc.name}: {acc.price} руб.")


# Создаем цветы
rose = Flower("Роза", 250, 100)
tulip = Flower("Тюльпан", 150, 50)
chrisantem = Flower( 'Хризантема', 200, 150)
gvozdika = Flower('Гвоздика', 130, 150)
craft_paper = Accessory("Крафтовая бумага", 150)
ribbon = Accessory("Атласная лента", 50)

# Формируем букет
my_bouquet = Bouquet()
my_bouquet.add_flower(rose, 5)
my_bouquet.add_flower(tulip, 3)
my_bouquet.add_flower(rose, 2)
my_bouquet.add_flower(chrisantem, 1)
my_bouquet.add_flower(gvozdika, 3)
my_bouquet.add_accessory(craft_paper)
my_bouquet.add_accessory(ribbon)

my_bouquet.show_bouquet()
# Сортировки
my_bouquet.show_sorted_by_price('ASC')
my_bouquet.show_sorted_by_price('DESC')

print("Итоговая стоимость букета (с учетом декора):", my_bouquet.total_price(), "руб.")
print(f"Среднее время жизни букета: {my_bouquet.get_life_time():.1f} ч.")

pion = Flower("Пион", 1, 1) #Проверка присутствия цветка (по виду) в букете

my_bouquet.has_flower(pion)
