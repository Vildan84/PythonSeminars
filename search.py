import csv


def search_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    with open('database.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Фамилия"] == surname.capitalize() and row["Имя"] == name.capitalize():
                print(row["Фамилия"], row["Имя"], row["Телефон"], row["Описание"])
                break
        else:
            print("Контакт не найден")