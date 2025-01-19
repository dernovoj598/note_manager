from datetime import datetime

current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(f"Текущая дата:{current_date.strftime('%d-%m-%Y')}")

while True:
    try:
        deadline_str = input("Введите дату дедлайна (в формате день-месяц-год, например 17.01.2025): ")
        deadline_date = datetime.strptime(deadline_str,"%d-%m-%Y")

        time_difference = deadline_date - current_date
        days_difference = time_difference.days

        if days_difference < 0:
            print(f"Внимание! Дедлайн истек {abs(days_difference):02d} дней назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {days_difference:02d} дней.")

            break

    except ValueError:
        print("Ошибка! Введите правильный формат даты (день-месяц-год).")
        print("Пример: 17-01-2025")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")


