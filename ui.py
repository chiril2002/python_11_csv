from logger import input_data,  print_data, delete_data, edit_data 


def interface():
    print('Здравствуйте Добрый день вы попали на специальный бот  правочник от Geekbrain! \n 1 - записи данных \n 2 - вывод даных \n 3 - Удалить даных \n 4 - Редактировать даных ')
    command  = int(input('введите число: '))
    
    
    while  command != 1 and command != 2 and command != 3 and command != 4 :
        print('error')
        command = int(input('введите число'))
    
    
    if command == 1:
        input_data()
    elif command == 2: 
        print_data()
    elif command == 3: 
        delete_data()
    elif command == 4: 
        edit_data()
