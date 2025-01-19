current_status = ("В процессе")

print(f"Текущий статус заметки: {current_status}")

new_status = input('''Выберите новый статус заметки:
1. Выполнено
2. В процессе
3. Отложено
''')

while new_status not in ["1", "2", "3"]:
    print("Неправильный ввод! Выберите числа от 1 до 3.")
    new_status = input('''Выберите новый статус заметки:
    1. Выполнено
    2. В процессе
    3. Отложено
    ''')

status_option = {'1': "Выполнено", '2': "В процессе", '3': "Отложено"}
current_status = status_option[new_status]

print(f"Статус заметки обновлен: {current_status}")