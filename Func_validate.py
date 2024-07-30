import json
def input_validate(type_input: str) -> str:
    """ Функция приглашает пользователя к вводу данных, проверяет 
        корректность введенных данных.
        type_input = menu - выводит приглашение для ввода пункта меню
        type_input = build - выводит приглашение для ввода кол-ва построек
        type_input = army - выводит приглашение для ввода кол-ва солдат
        type_input = sale - выводит приглашение для ввода кол-ва единиц 
        товаров для продажи на рынке"""
        
    answer_dict = {'menu':'Введите номер пункта меню для его выбора >> ',
                   'build':'Введите кол-во для постройки >> ',
                   'army':'Введите кол-во солдат для найма >> ',
                   'sale':'Введите кол-во единиц для продажи >> '}
                   
    
    # запускаем бесконечный цикл
    while True:
    
        # приглашаем пользователя к вводу данных
        input_num = input(f'{answer_dict.get(type_input)}')
        
        if input_num.isdigit():
            return input_num # если все ок, то возвращаем введеное значение
        
        print('Ошибка ввода, введите число')
        print()



# class Menu:
    

with open('all_menu_objects3.json', 'r', encoding = 'utf-8') as file:
    a = json.load(file)

for i in a.values():
    print(i)

# with open('new_json.json','w', encoding = 'utf-8') as raw:
    # json.dump(a, raw, ensure_ascii=False)


# with open('new_json.json','w', encoding = 'utf-8') as raw:
    # json.dump(a, raw, ensure_ascii=False)