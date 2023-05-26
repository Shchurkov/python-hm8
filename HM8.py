def display_contacts():
    with open("phonebook.txt", "r") as file:
        contacts = file.readlines()  # Читаем все строки из файла
        if contacts:  # Если список контактов не пустой
            print("Телефонный справочник:")
            for contact in contacts:  # Проходим по каждому контакту в списке
                # Разбиваем строку на отдельные поля (фамилия, имя, отчество, номер телефона)
                surname, name, patronymic, phone_number = contact.strip().split(",")
                # Выводим информацию о контакте
                print(f"Фамилия: {surname}, Имя: {name}, Отчество: {patronymic}, Номер телефона: {phone_number}")
        else:
            print("Телефонный справочник пуст.")


def save_contacts(contacts):
    with open("phonebook.txt", "w") as file:
        for contact in contacts:  # Проходим по каждому контакту в списке
            # Записываем данные контакта в файл в формате: фамилия,имя,отчество,номер телефона
            file.write(contact)


def search_contacts():
    search_criteria = input("Введите критерий поиска (фамилию или имя): ")
    with open("phonebook.txt", "r") as file:
        contacts = file.readlines()  # Читаем все строки из файла
        found_contacts = []  # Создаем пустой список для найденных контактов
        for contact in contacts:  # Проходим по каждому контакту в списке
            surname, name, patronymic, phone_number = contact.strip().split(",")
            # Проверяем, содержит ли контакт заданный критерий поиска
            if search_criteria.lower() in [surname.lower(), name.lower()]:
                found_contacts.append(contact)  # Добавляем найденный контакт в список найденных контактов

        if found_contacts:  # Если список найденных контактов не пустой
            print("Результаты поиска:")
            for contact in found_contacts:  # Проходим по каждому найденному контакту
                surname, name, patronymic, phone_number = contact.strip().split(",")
                # Выводим информацию о найденном контакте
                print(f"Фамилия: {surname}, Имя: {name}, Отчество: {patronymic}, Номер телефона: {phone_number}")
        else:
            print("Ничего не найдено.")


def edit_contact():
    search_criteria = input("Введите имя или фамилию контакта для редактирования: ")
    with open("phonebook.txt", "r") as file:
        contacts = file.readlines()

    found_contacts = []
    for contact in contacts:
        surname, name, patronymic, phone_number = contact.strip().split(",")
        # Проверяем, содержит ли контакт заданный критерий поиска
        if search_criteria.lower() in [surname.lower(), name.lower()]:
            found_contacts.append(contact)

    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(f"{i + 1}. {contact.strip()}")

        choice = int(input("Введите номер контакта, который хотите отредактировать: "))
        if 1 <= choice <= len(found_contacts):
            surname, name, patronymic, phone_number = found_contacts[choice - 1].strip().split(",")
            new_surname = input(f"Текущая фамилия: {surname}. Введите новую фамилию (или оставьте пустым): ")
            new_name = input(f"Текущее имя: {name}. Введите новое имя (или оставьте пустым): ")
            new_patronymic = input(f"Текущее отчество: {patronymic}. Введите новое отчество (или оставьте пустым): ")
            new_phone_number = input(f"Текущий номер телефона: {phone_number}. Введите новый номер телефона (или оставьте пустым): ")

            if new_surname:
                surname = new_surname
            if new_name:
                name = new_name
            if new_patronymic:
                patronymic = new_patronymic
            if new_phone_number:
                phone_number = new_phone_number

            found_contacts[choice - 1] = f"{surname},{name},{patronymic},{phone_number}\n"

            save_contacts(contacts)  # Сохраняем измененные контакты в файл
            print("Контакт успешно отредактирован!")
        else:
            print("Неверный выбор.")
    else:
        print("Контакт не найден.")


def delete_contact():
    search_criteria = input("Введите имя или фамилию контакта для удаления: ")
    with open("phonebook.txt", "r") as file:
        contacts = file.readlines()

    found_contacts = []
    for contact in contacts:
        surname, name, patronymic, phone_number = contact.strip().split(",")
        # Проверяем, содержит ли контакт заданный критерий поиска
        if search_criteria.lower() in [surname.lower(), name.lower()]:
            found_contacts.append(contact)

    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(f"{i + 1}. {contact.strip()}")

        choice = int(input("Введите номер контакта, который хотите удалить: "))
        if 1 <= choice <= len(found_contacts):
            contacts.remove(found_contacts[choice - 1])

            save_contacts(contacts)  # Сохраняем измененные контакты в файл
            print("Контакт успешно удален!")
        else:
            print("Неверный выбор.")
    else:
        print("Контакт не найден.")


def menu():
    while True:
        print("\nТелефонный справочник")
        print("1. Вывести все контакты")
        print("2. Поиск контакта")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            display_contacts()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор.")


menu()
