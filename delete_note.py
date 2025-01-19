notes = [
    {
        'id': 1,
        'username': 'Данила',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю'
    },
    {
        'id': 2,
        'username': 'Мария',
        'title': 'Учеба',
        'description': 'Подготовиться к экзамену',
    },
    {
        'id': 3,
        'username': 'Алексей',
        'title': 'Встреча',
        'description': 'Встреча с друзьями'
    }
]

print("Текущие заметки:")
for note in notes:
    print(f"{note['id']}. Имя:{note['username']}")
    print(f"Заголовок:{note['title']}")
    print(f"Описание:{note['description']}\n")

search_term = input("Введите имя пользователя или заголовок для удаления заметки: ")

if not search_term:
    print("Ошибка: критерий поиска не может быть пустым.")
else:
    notes_to_keep = []
    notes_to_delete = []

    for note in notes:
        if note['username'] == search_term or note['title'] == search_term:notes_to_delete.append(note)
        else:notes_to_keep.append(note)

    if not notes_to_delete:
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    else:
        print("\nСледующие заметки будут удалены:")
        for note in notes_to_delete:
         print(f"{note['id']}. Имя:{note['username']}")
         print(f"Заголовок:{note['title']}")
         print(f"Описание:{note['description']}\n")

         confirm = input("Вы уверены, что хотите удалить эти заметки? (да/нет): ")

         if confirm == 'да':
             notes = notes_to_keep
             for i, note in enumerate(notes, 1):
                 note['id'] = i

                 print("\nЗаметки успешно удалены.")
                 if notes:
                     print("\nОстались следующие заметки:")
                     for note in notes:
                         print(f"{note['id']}. Имя: {note['username']}")
                         print(f"Заголовок:{note['title']}")
                         print(f"Описание:{note['description']}\n")
                     else:
                         print("Список заметок пуст.")
                 else:
                     print("\nУдаление отменено.")





