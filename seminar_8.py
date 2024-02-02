from typing import List


def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    # search_idx
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def copy_data(file_on, file_in):
    data = list(enumerate(read_file(file_in)))
    
    print("Выберите номер строки, которую надо скопировать:")
    for i in data:
        print(f"{i[0]} -- {i[1]}")
        
    num = int(input("Номер строки: "))
    while num >= len(data):
        print("Не верный номер строки")
        num = int(input("Номер строки: "))
    
    with open(file_on, 'a', encoding='utf-8') as f:
        f.write("\n" + data[num][1])

def main():
    file_name = input("Введите имя файла: ")
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - скопировать данные')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            file_name2 = input("Введите имя файла из которого будет копирование: ")
            copy_data(file_name, file_name2)
            

if __name__ == '__main__':
    main()
