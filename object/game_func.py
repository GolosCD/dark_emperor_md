import json


def input_validate(type_input: str) -> str:
    """ Функция приглашает пользователя к вводу данных, проверяет 
      корректность введенных данных.
      type_input = menu - выводит приглашение для ввода пункта меню
      type_input = build - выводит приглашение для ввода кол-ва построек
      type_input = army - выводит приглашение для ввода кол-ва солдат
      type_input = sale - выводит приглашение для ввода кол-ва единиц 
      товаров для продажи на рынке"""

    answer_dict = {
        'menu': 'Введите номер пункта меню для его выбора >> ',
        'build': 'Введите кол-во для постройки >> ',
        'army': 'Введите кол-во солдат для найма >> ',
        'sale': 'Введите кол-во единиц для продажи >> '
    }
    # запускаем бесконечный цикл
    while True:

        # приглашаем пользователя к вводу данных
        input_num = input(f'{answer_dict.get(type_input)}')

        if input_num.isdigit():
            return input_num  # если все ок, то возвращаем введеное значение

        print('Ошибка ввода, введите число')
        print()


def menu_input_validate(menu_keys) -> bool:
    """ Функция проверяет введеное пользователем значение на принадлежность к
        пунктам меню, которое он хочет вызвать"""

    while True:

        # приглашаем пользователя к вводу данных
        user_num = input_validate('menu')

        if user_num in menu_keys:
            return user_num
        else:
            print('Ошибка ввода, выберете один из пунктов меню')
            continue

def json_loader (file_path: str) -> dict:
    """ Функция загружает меню из json"""
    
    with open(file_path,'r',encoding='utf=8') as raw:
           return json.load(raw)