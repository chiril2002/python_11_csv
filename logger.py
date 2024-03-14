from date_create import name_data , surname_data ,phone_data, address_data

def input_data(): 
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    
    var = int(input(f"В каком формате записать данных \n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант:  \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"Выберите вариант: "))
    
    
    while var != 1 and var != 2:
        print('Неправильный вывод')
        var = int(input('Введите число: '))
    if var == 1:
        with open('date_first_varint.csv', 'a', encoding='utf-8' ) as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
            
    elif var == 2:
        with open('date_sacond_varint.csv', 'a', encoding='utf-8' ) as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")                
    
    
    
def print_data():
    print('Вывожу данных с 1 файла: \n')
    with open('date_first_varint.csv', 'r', encoding='utf-8' ) as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0 
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
                
        print(''.join(data_first_list))
        
        
    
    print('Вывожу данных с 1 файла: \n')
    with open('date_sacond_varint.csv', 'r', encoding='utf-8' ) as f:
        date_sacond = f.readlines()
        print(*date_sacond)
        


def delete_data():
    print('Что будете  удалять ? \n 1 имя \n 2 Фамилию \n 3 телефон \n 4 адрес \n ')
    a  = int(input())
    while  a != 1 and a != 2 and a != 3 and a != 4 :
        print('error')
        a = int(input('введите число'))
    
    
    if a == 1:
        name = input("Ведите ваше имя:")
    elif a == 2: 
        name = input("Ведите ваше Фамилию:")
    elif a == 3: 
        name = input("Ведите ваше телефон:")
    elif a == 4: 
        name = input("Ведите ваше адрес:")
    
    
    found = False  # Флаг для отслеживания нахождения имени в файле

    with open('date_first_varint.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        
        

    with open('date_first_varint.csv',  'w', encoding='utf-8') as f:
        for line in data_first :
            if name not in line:
                f.write(line)
            else:
                found = True
                
                
    with open('date_sacond_varint.csv',  'r', encoding='utf-8') as f:
        data_sacond = f.readlines()
        
                    
    with open('date_sacond_varint.csv',  'w', encoding='utf-8') as f:
        for line in data_sacond :
            if name not in line:
                f.write(line)
            else:
                found = True            

    if not found:
        print(f"Контакт {name} не найден в справочнике")
    else:
        print(f"Контакт {name} успешно удален из справочника")






import os

def edit_data():
    print('Введите ваше имя: ')
    name = input()
    
    found = False  # Флаг для отслеживания нахождения имени в файле

    temp_file = 'temp.csv'  # Имя временного файла

    with open('date_first_varint.csv', 'r', encoding='utf-8') as f_in, open(temp_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if name not in line:
                f_out.write(line)
            else:
                found = True
                name_new = input('Введите ваше имя: ')
                # Добавляем новое имя в исходный файл
                f_out.write(f"{name_new}\n")

    if not found:
        print(f"Контакт {name} не найден в справочнике")
    else:
        print(f"Контакт {name} успешно отредактирован в справочнике")

    # Заменяем содержимое исходного файла содержимым временного файла
    os.remove('date_first_varint.csv')  # Удаляем оригинальный файл
    os.rename(temp_file, 'date_first_varint.csv')  # Переименовываем временный файл
