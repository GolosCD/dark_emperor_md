from object.game_func import *

param = json_loader('object/param.json')

########_Printer_##############################################################################  
class Printer:
  """Класс для печати разделов меню"""
  def __init__ (self):
    self.menu_objects = json_loader('object/menu.json')
    # self.type_menu = {'1':'main','2':'build','3':'trade','4':'army','5':'food','6':'taxes',}

  def menu (self, name: str):
      """Метод печатает меню"""

      for num, name_line in self.menu_objects.get(name).items():
          print(f'{num} - {name_line}')
        
  @classmethod
  def menu_cls (cls, name: str):
    """Метод печатает меню"""
    menu_objects = json_loader('object/menu.json')
    for num, name_line in menu_objects.get(name).items():
        print(f'{num} - {name_line}')
#############################################################################################    



class ControlManager:
  printer = Printer()

  @classmethod
  def print_main_menu(cls): # и печать основного меню и начало игры
    
    Printer.menu_cls('main')

    num = input_validate('menu')
    
    try:
      actions_main[num]()
    except:
      print("Invalid selection, please try again.\n")
      cls.print_main_menu()
    
  @classmethod
  def print_build_menu(cls):
    
    Printer.menu_cls('build')
    
    num = input_validate('menu')
    actions_build[num]()
    
    try:
      actions_build[num]()
    except:
       print("Invalid selection, please try again(*).\n")
       cls.print_build_menu()
      
      
  

  @classmethod
  def print_trade_menu(cls):
    Printer.menu_cls('trade')
  
########_Treasury_##########################################################################
class Treasury: # Казна королевства
  current_count_gold = param.get('user_resurce').get('gold_float')

  @classmethod
  def current_gold(cls):
    """Метод возвращает текущее кол-во золота в казне королевства"""
    return cls.current_count_gold

  @classmethod
  def write_off_gold(cls, price):
    """Метод списывает указанную сумму из казны королевства"""
    cls.current_count_gold -= price

  @classmethod
  def write_on_gold(cls, price):
    """Метод записывает указанную сумму в казну королевства"""
    cls.current_count_gold += price
#############################################################################################

########_Informer_###########################################################################
class Informer: # Информер

  @classmethod
  def no_gold(cls):
    print('Need more gold')
    input('Нажмите Enter для продолжения')

#############################################################################################


class Builder:

  @classmethod
  def farm (cls):
    """Метод постройки фермы"""
    build_name = 'farm'
    
    # просим ввести кол-во ферм к постройке
    print(f'Тут будет инфа о текущем кол-ве ферм, стоимость 1 фермы, текущее золото, и макс. кол-во к постройке')
    
    qty_farm =  int(input_validate('build'))

    # Считаем общую стоимость требуемых построек
    build_count_price_float = cls.calc_cost_build(build_name,qty_farm)

    if build_count_price_float<=Treasury.current_gold():# если деняк в казне хватает

      # то увеличиваем кол-во ферм
      cls.change_count_build(build_name,qty_farm,'+')

      # списываем деньги за успешное строительство фермы
      Treasury.write_off_gold(build_count_price_float)
      
      print(f'Вы построили {qty_farm} ферм')
      ControlManager.print_build_menu()

    else:
      # Уведомление, что нехватает денег
      Informer.no_gold()
      #Printer.menu_cls('build')
      ControlManager.print_build_menu()
      

  @classmethod
  def calc_cost_build(cls, build_name, qty):
    """Метод подсчета стоимости указанных построек"""
    return float(qty) * param.get(build_name).get('price_float')

  @classmethod
  def change_count_build(cls,build_name, qty, mark):
    """Метод меняет кол-во построек в хранилище,
       если mark = + увеличиваем кол-во построе
       иначе уменьшаем кол-во построек"""
    
    if mark == '+': # если + то операция увеличения кол-ва зданий
      param[build_name]['count_int'] += qty
    else:
      if param[build_name]['count_int'] < qty: # если кол-во построек меньше чем указанное кол
        param[build_name]['count_int'] = 0
      else:
        param[build_name]['count_int'] -= qty
    
#######_ACTIONS_################################################################################
actions_main = {'1':'Экшен с окончание хода',
                '2':ControlManager.print_build_menu,
                '3':ControlManager.print_trade_menu,}

actions_build = {'1': Builder.farm,
                 '2':'Builder.market',
                 '0':ControlManager.print_main_menu}
################################################################################################


#Запуск
ControlManager.print_main_menu()