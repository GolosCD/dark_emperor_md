from object.game_func import *
from object.game_object import *

#загружаем параметры игры
param = json_loader('object/param.json')

#Инициализация экземпляров
#Постройки
farm = ConstructionObject('farm', *param['farm'].values())
market = ConstructionObject('market', *param['market'].values())
mine = ConstructionObject('mine', *param['mine'].values())
blacksmith = ConstructionObject('blacksmith', *param['blacksmith'].values())
castl = ConstructionObject('castl', *param['castl'].values())
#Казна
treasury = Treasury(param.get('kingdom').get('gold'))


########_Printer_##############################################################################
class Printer:
  """Класс для печати разделов меню"""

  menu_objects = json_loader('object/menu.json')  # загружаем меню из json

  @classmethod
  def menu(cls, name: str):
    """Метод печатает меню"""

    for num, name_line in cls.menu_objects.get(name).items():
      print(f'{num} - {name_line}')


#############################################################################################


class ControlManager:

  @classmethod
  def print_main_menu(cls):  # и печать основного меню и начало игры

    Printer.menu('main')

    num = input_validate('menu')

    try:
      actions_main[num]()
    except KeyError:
      print("Invalid selection, please try again.\n")
      cls.print_main_menu()

  @classmethod
  def print_build_menu(cls):

    Printer.menu('build')

    num = input_validate('menu')

    try:
      actions_build[num](farm)
    except KeyError:
      print("Invalid selection, please try again(*).\n")
      cls.print_build_menu()

  @classmethod
  def print_trade_menu(cls):
    Printer.menu('trade')


########_Informer_###########################################################################
class Informer:  # Информер

  @classmethod
  def no_gold(cls):
    print('Need more gold')
    input('Нажмите Enter для продолжения')


#############################################################################################


class Builder:

  @classmethod
  def create_build(cls, obj: ConstructionObject):
    """Метод постройки фермы"""
    build_name = obj.name

    # просим ввести кол-во ферм к постройке
    print(
        f'Тут будет инфа о текущем кол-ве ферм, стоимость 1 фермы, текущее золото, и макс. кол-во к постройке'
    )

    qty_farm = input_validate('build')

    # Считаем общую стоимость требуемых построек
    total_price = obj.get_current_price() * qty_farm

    if total_price <= treasury.get_current_gold(
    ):  # если деняк в казне хватает

      # то увеличиваем кол-во ферм
      farm.add_count_build(qty_farm)
      # cls.change_count_build(build_name,qty_farm,'+')

      # списываем деньги за успешное строительство фермы
      treasury.remove_gold(total_price)

      print(f'Вы построили {qty_farm} ферм')
      ControlManager.print_build_menu()

    else:
      # Уведомление, что нехватает денег
      Informer.no_gold()
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
