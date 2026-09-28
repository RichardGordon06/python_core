# Шаг 1: Читаем бинарные данные из обоих файлов в память
with open('first.bin', "rb") as file_1:
    data_from_file_1 = file_1.read()

with open('second.bin', "rb") as file_2:
    data_from_file_2 = file_2.read()

# Шаг 2: Записываем данные крест-накрест (меняем содержимое местами)
with open('first.bin', "wb") as file_1:
    file_1.write(data_from_file_2)

with open('second.bin', "wb") as file_2:
    file_2.write(data_from_file_1)

print("Содержимое бинарных файлов успешно изменено местами, проверьте содержимое:)")