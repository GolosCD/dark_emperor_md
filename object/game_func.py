import json


def input_validate(type_input: str) -> str|int:
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
        print()
        
        if input_num.isdigit():
            if type_input == 'menu':
                return input_num  # для menu вернем str
            else:
                return int(input_num)  # иначе int


        print('Ошибка ввода, введите число')
        print()


def json_loader(file_path: str) -> dict:
    """ Функция загружает меню из json"""

    with open(file_path, 'r', encoding='utf=8') as raw:
        return json.load(raw)
