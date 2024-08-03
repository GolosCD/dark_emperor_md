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
    """Метод запускает начало игру (тут все начинается)"""

    printer.welcome()

    printer.menu('main')

    num = input_validate('menu')

    try:
      actions_main[num]()
    except KeyError:
      print("Invalid selection, please try again.\n")
      cls.print_main_menu()

  @classmethod
  def print_main_menu(cls):  # и печать основного меню и начало игры

    printer.menu('main')

    num = input_validate('menu')

    try:
      actions_main[num]()
    except KeyError:
      print("Invalid selection, please try again.\n")
      cls.print_main_menu()

  @classmethod
  def print_build_menu(cls):

    printer.menu('build')

    num = input_validate('menu')

    try:
      actions_build[num](farm)
    except KeyError:
      print("Invalid selection, please try again(*).\n")
      cls.print_build_menu()

  @classmethod
  def back(cls):
    cls.print_build_menu()
    

  @classmethod
  def print_trade_menu(cls):
    printer.menu('trade')


class Builder:

  @classmethod
  def create_build(cls, obj: ConstructionObject):
    """Метод постройки фермы"""

    # просим ввести кол-во ферм к постройке
    qty_farm = input_validate('build')

    # Считаем общую стоимость требуемых построек
    total_price = obj.get_current_price() * qty_farm

    if total_price <= treasury.get_current_gold():  # если деняк в казне хватает

      # то увеличиваем кол-во ферм
      farm.add_count_build(qty_farm)

      # списываем деньги за успешное строительство фермы
      treasury.remove_gold(total_price)

      print(f'Вы построили {qty_farm} ферм')
      ControlManager.print_build_menu()

    else:
      # Уведомление, что нехватает денег
      info.no_gold()
      #Printer.menu('build')
      ControlManager.print_build_menu()


#######_ACTIONS_################################################################################
actions_main = {
    '1': 'Экшен с окончание хода',
    '2': ControlManager.print_build_menu,
    '3': ControlManager.print_trade_menu,
}

actions_build = {
    '1': Builder.create_build,
    '2': 'Builder.market',
    '0': ControlManager.print_main_menu
}
################################################################################################
