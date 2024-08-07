from object.game_func import *
from object.game_object import *
import sys
import subprocess # Проверь меня


# загружаем параметры игры
settings = json_loader('object/settings.json')

# Инициализация экземпляров
# Постройки
farm       = Build('farm', *settings['farm'].values())
market     = Build('market', *settings['market'].values())
mine       = Build('mine', *settings['mine'].values())
blacksmith = Build('blacksmith', *settings['blacksmith'].values())
castl      = Build('castl', *settings['castl'].values())
# Словарь с экземплярами построек, для дальнейшей передачи в функцию строительства
object_for_build = {'1':farm, '2':market, '3':mine, '4':blacksmith, '5':castl}
# Казна
treasury = Treasury(settings.get('kingdom').get('gold'))
# Уведомлялка
info = Informer()
# Принтер
printer = Printer(json_loader('object/menu.json'))


class ControlManager:

  @classmethod
  def start_game(cls):
    """Метод запускает начало игры (тут все начинается)"""
    
    subprocess.run('clear', shell=True) # Проверь меня
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

    # печать пунктов строительного меню
    printer.menu('build')
     # приглашение к выбору пункта меню
    num = input_validate('menu')

    try:
      if num in object_for_build:
        # выбор экшен функции
        build_actions[num](object_for_build[num])
      elif num =='0':
        build_actions[num]() # если 0, то возвращаемся назад из строительного меню
      else:
        raise KeyError()
    except KeyError:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов строительного меню
      cls.print_build_menu()

  @classmethod
  def back_to_main(cls):
    """Метод просто возвращается в основное меню"""
    
    cls.print_main_menu()

  @classmethod
  def print_trade_menu(cls):
    """Метод печатает пункты торгового меню
     и приглашение к выбору пункта меню"""
    
    # печать пунктов торгового меню
    printer.menu('trade')
     # приглашение к выбору пункта меню
    num = input_validate('menu')

    try:
      # выбор экшен функции
      trade_actions[num]()
    except KeyError:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов торгового меню
      cls.print_build_menu()

  @classmethod
  def print_food_menu(cls):
    """Метод печатате пункты торгового меню
       и приглашение к выбору пункта меню"""

    # печать пунктов меню распределение еды
    printer.menu('food')
    # приглашение к выбору распределения кол-ва еды
    num = input_validate('menu')

    try:
      # выбор экшен функции
      food_actions[num]()
    except:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов меню распределения еды
      cls.print_food_menu()

  @classmethod
  def print_taxes_menu(cls):
    """Метод печатате пункты налогового меню
       и приглашение к выбору пункта меню"""

    # печать пунктов налогового меню
    printer.menu('taxes')
    # приглашение к выбору уровня налогов
    num = input_validate('menu')

    try:
      # выбор экшен функции
      taxes_actions[num]()
    except:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов меню налогового меню
      cls.print_taxes_menu()

  @classmethod
  def print_end_round_menu(cls):
    """Метод печатате пункты меню завершения хода
       и приглашение к выбору пункта меню"""

    # печать пунктов меню завершения хода
    printer.menu('end_round')
    # приглашение к выбору пункта
    num = input_validate('menu')

    try:
      # выбор экшен функции
      end_round_actions[num]()
    except:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов меню завершения хода
      cls.print_end_round_menu()

  @classmethod
  def print_end_game_menu(cls):
    """Метод печатате пункты налогового меню
       и приглашение к выбору пункта меню"""

    # печать пунктов налогового меню
    printer.menu('end_game')
    # приглашение к выбору уровня налогов
    num = input_validate('menu')

    try:
      # выбор экшен функции
      end_game_actions[num]()
    except:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов меню налогового меню
      cls.print_end_game_menu()


class Builder:

  @classmethod
  def create_build(cls, obj: Build):
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

      print(f'Вы построили {qty_obj} шт. выбранных объектов','\n')

    else:
      # Уведомление, что нехватает денег
      info.no_gold()
      
    #По окончанию строительных работ, вызывается меню строительства
    ControlManager.print_build_menu()


#######_ЭКШОНЧИКИ_#############################
main_actions = {
    '1': ControlManager.print_end_round_menu,
    '2': ControlManager.print_build_menu,
    '3': ControlManager.print_trade_menu,
    '4': lambda: print('Функция наема армии не доступна','\n'),
    '5': ControlManager.print_food_menu,
    '6': ControlManager.print_taxes_menu,
    '7': lambda: print('Функция советника не доступна','\n'),
    '8': lambda: print('Функция печати отчета не доступна','\n'),
    '9': ControlManager.print_end_game_menu,
}

build_actions = {
    '1': Builder.create_build,
    '2': Builder.create_build,
    '3': Builder.create_build,
    '4': Builder.create_build,
    '5': Builder.create_build,
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
    '1': lambda: print('Услуги советника не доступны','\n'),
    '0': ControlManager.back_to_main
}

report_actions = {
    '1': lambda: print('Услуга печати отчета не доступна','\n'),
    '0': ControlManager.back_to_main
}

end_game_actions = {
    '1': sys.exit,
    '0': ControlManager.back_to_main
}

end_round_actions = {
    '1': lambda: print('Функция завершения года не доступна','\n'),
    '0': ControlManager.back_to_main
}

################################################
