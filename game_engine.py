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
treasury = Kingdom(settings.get('kingdom').get('gold'))
# Жители
villager = Kingdom(settings.get('kingdom').get('villager'))
# Армия
army = Kingdom(settings.get('kingdom').get('army'))
# Уведомлялка
info = Informer()
# Принтер
printer = Printer(json_loader('object/menu.json'))
# Рацион
ration = Ration(settings['ration'])
# Налоги
taxes = Taxes(settings['taxes'])

# Пщеница
food = Resource('Пщеница', 
                 settings.get('resources').get('food'),
                 settings.get('price_sale').get('food'))
# Железная руда
iron_ore = Resource("Железная руда",
                     settings.get('resources').get('iron_ore'),
                     settings.get('price_sale').get('iron_ore'))
# Оружие
weapen = Resource("Оружие",
                   settings.get('resources').get('weapon'),
                   settings.get('price_sale').get('weapon'))


#Игровой год
year = Year(settings.get('year').get('game_year'),
            settings.get('year').get('end_year'),
            settings.get('year').get('harvest_key'))

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
      cls.print_trade_menu()

  @classmethod
  def print_ration_menu(cls):
    """Метод печатате пункты торгового меню
       и приглашение к выбору пункта меню"""

    # печать пунктов меню распределение еды
    printer.menu('ration')
    # приглашение к выбору распределения кол-ва еды
    num = input_validate('menu')

    try:
      # выбор экшен функции
      ration_actions[num](num)
      print(ration.get_k_ration())
    except:
      #  Уведомление о том, что криво выбран пункт меню
      printer.incorrect_key()
      # Повторный вызов меню распределения еды
      cls.print_ration_menu()

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
      taxes_actions[num](num)
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

####################----------#########################

# пока тут отчетная дичь для проверки обьектов разных классов
  @classmethod
  def print_report_menu(cls):
    """Метод распечатки отчета"""
    
    print('Отчет')
    print('Сейчас какой-то год от какого-то события')
    print()
    print(gold, food, villager, iron_ore, weapen, army, sep='\n')
    print()
    print(*object_for_build.values(), sep='\n')
    

    print()
    printer.menu('report')

    while True:
      num = input_validate('menu')
      if num == '0':
        cls.print_main_menu()

#########################-----------#########################  
  
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

    if total_price <= treasury.get_count():  # если деняк в казне хватает

      # то увеличиваем кол-во ферм
      farm.add_count_build(qty_obj)

      # списываем деньги за успешное строительство фермы
      treasury.remove(total_price)

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
    '5': ControlManager.print_ration_menu,
    '6': ControlManager.print_taxes_menu,
    '7': lambda: print('Функция советника не доступна','\n'),
    '8': ControlManager.print_report_menu,
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

ration_actions = {
    '1': ration.set_k_ration,
    '2': ration.set_k_ration,
    '3': ration.set_k_ration,
    '4': ration.set_k_ration,
    '5': ration.set_k_ration,
    '0': ControlManager.back_to_main
}

taxes_actions = {
    '1': taxes.set_k_taxes,
    '2': taxes.set_k_taxes,
    '3': taxes.set_k_taxes,
    '4': taxes.set_k_taxes,
    '5': taxes.set_k_taxes,
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
