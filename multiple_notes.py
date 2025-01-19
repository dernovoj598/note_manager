from datetime import datetime

current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(f"Текущая дата:{current_date.strftime('%d-%m-%Y')}")

notes = []
print('Добро пожаловать в "Менеджер заметок!"')

while True:
    choice = input("Хотите добавить новую заметку? (да/нет): ").lower()

    if choice == "нет":
        print("Хорошего дня!")
        break

    elif choice == "да":
        while True:
            username = input("Ваше имя")
            if not username:
                print("Имя пользователя не может быть пустым! Пожалуста, введите ваще имя!")
            else:
                break

        while True:
            title = input("Заголовок заметки: ")
            if not title:
                print("Заголовок не может быть пустым! Пожалуйста, введите заголовок заметки!")
            else:
                break
