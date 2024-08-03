from object.game_func import *
from object.game_object import *

#загружаем параметры игры
param = json_loader('object/param.json')

#Инициализация экземпляров
#Постройки
farm       = ConstructionObject('farm', *param['farm'].values())
market     = ConstructionObject('market', *param['market'].values())
mine       = ConstructionObject('mine', *param['mine'].values())
blacksmith = ConstructionObject('blacksmith', *param['blacksmith'].values())
castl      = ConstructionObject('castl', *param['castl'].values())
#Казна
treasury = Treasury(param.get('kingdom').get('gold'))
# Уведомлялка
info = Informer()
# Принтер
printer = Printer(json_loader('object/menu.json'))


class ControlManager:

  @classmethod
  def start_game(cls):
    """Метод запускает начало игры (тут все начинается)"""

    # печать приветственного сообщения
    printer.welcome()
    # печать пунктов основного меню
    printer.menu('main')
    # приглашение к выбору пункта меню
    num = input_validate('menu')

    try:
      # выбор экшен функции
      main_actions[num]()
    except KeyError:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов основного меню
      cls.print_main_menu()

  @classmethod
  def print_main_menu(cls):
    """Метод печатает пункты основного меню 
       и приглашение к выбору пункта меню"""

    # печать пунктов основного меню
    printer.menu('main')
    # приглашение к выбору пункта меню
    num = input_validate('menu')

    try:
      # выбор экшен функции
      main_actions[num]()
    except KeyError:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов основного меню
      cls.print_main_menu()

  @classmethod
  def print_build_menu(cls):
    """Метод печатает пункты строительного меню
       и приглашение к выбору типа постройки"""

    # словарь с экземпллярами, для дальнейшей передачи в функцию строительства
    object_for_build = {
                        '1':farm,
                        '2':market,
                        '3':mine,
                        '4':blacksmith,
                        '5':castl
                       }

    # печать пунктов строительного меню
    printer.menu('build')
     # приглашение к выбору пункта меню
    num = input_validate('menu')

    try:
      # выбор экшен функции
      build_actions['1'](object_for_build[num])
    except KeyError:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов строительного меню
      cls.print_build_menu()

  @classmethod
  def back_to_main(cls):
    """Метод просто возвращается в основное меню"""
    
    cls.print_build_menu()

  @classmethod
  def print_trade_menu(cls):
    """Метод печатает пункты торгового меню
     и приглашение к выбору пункта меню"""
    
    # печать пунктов торгового меню
    printer.menu('build')
     # приглашение к выбору пункта меню
    num = input_validate('menu')

    try:
      # выбор экшен функции
      trade_actions[num]()
    except KeyError:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов строительного меню
      cls.print_build_menu()



class Builder:

  @classmethod
  def create_build(cls, obj: ConstructionObject):
    """Метод постройки фермы"""

    # просим ввести кол-во ферм к постройке
    qty_obj = input_validate('build')

    # Считаем общую стоимость требуемых построек
    total_price = obj.get_current_price() * qty_obj

    if total_price <= treasury.get_current_gold():  # если деняк в казне хватает

      # то увеличиваем кол-во ферм
      farm.add_count_build(qty_obj)

      # списываем деньги за успешное строительство фермы
      treasury.remove_gold(total_price)

      print(f'Вы построили {qty_obj} выбранных объектов')
      ControlManager.print_build_menu()

    else:
      # Уведомление, что нехватает денег
      info.no_gold()
      #Printer.menu('build')
      ControlManager.print_build_menu()


#######_ЭКШОНЧИКИ_#############################
main_actions = {
    '1': lambda: print('Функция окончания года не доступна','\n'),
    '2': ControlManager.print_build_menu,
    '3': ControlManager.print_trade_menu,
    '4': lambda: print('Функция наема армии не доступна','\n'),
    '5': lambda: print('Функция распределения пищи не доступна','\n'),
    '6': lambda: print('Функция управления налогами не доступна','\n'),
    '7': lambda: print('Функция советника не доступна','\n'),
    '8': lambda: print('Функция печати отчета не доступна','\n'),
    '9': lambda: print('Функция управления игрой не доступна','\n'),
}

build_actions = {
    '1': Builder.create_build,
    '0': ControlManager.back_to_main
}

trade_actions = {
    '1': lambda: print('Продажа пшеницы не доступна','\n'),
    '2': lambda: print('Продажа железной руды не доступна','\n'),
    '3': lambda: print('Продажа оружия не доступна','\n'),
    '0': ControlManager.back_to_main
}

food_actions = {
    '1': lambda: print('Распределление очень малого кол-ва еды не доступна','\n'),
    '2': lambda: print('Распределление малого кол-ва еды не доступна','\n'),
    '3': lambda: print('Распределление среднего кол-ва еды не доступна','\n'),
    '4': lambda: print('Распределление большого кол-ва еды не доступна','\n'),
    '5': lambda: print('Распределление очень большого кол-ва еды не доступна','\n'),
    '0': ControlManager.back_to_main
}

taxes_actions = {
    '1': lambda: print('Установка очень низких налогов не доступна','\n'),
    '2': lambda: print('Установка низких налогов не доступна','\n'),
    '3': lambda: print('Установка средних налогов не доступна','\n'),
    '4': lambda: print('Установка высоких налогов не доступна','\n'),
    '5': lambda: print('Установка очень высоких налогов не доступна','\n'),
    '0': ControlManager.back_to_main
}

consultant_actions = {
    '1': lambda: print('Услуги советника недоступны','\n'),
    '0': ControlManager.back_to_main
}

report_actions = {
    '1': lambda: print('Услуга печати отчета недоступна','\n'),
    '0': ControlManager.back_to_main
}

end_actions = {
    '1': lambda: print('Запуск остановки игры недоступна','\n'),
    '0': ControlManager.back_to_main
}
################################################
