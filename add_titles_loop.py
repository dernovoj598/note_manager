title_list = []

title1 = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
while title1 != "":
    title_list.append(title1)
    title1 = input("Введите заголовок заметки (или оставьте пустым для завершения): ")

print("Заголовки: ")
for title1 in title_list:
    print(title1)
