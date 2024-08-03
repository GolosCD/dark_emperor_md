import json
#from game_func import input_validate

#from t import building_market

with open('object/menu.json', 'r', encoding='utf-8') as raw:
  menu = json.load(raw)


def print_menu(type_menu: str):
  for num, name in menu.get(type_menu).items():
    print(f'{num} -- {name}')


'''
action_menu = {'print_main_menu': 'menu',
               '1': 'Этого раздела еще нет!',
               '2': 'build_menu'
               # '3': print_menu('trade_menu'),
               # '4': print_menu('army_menu'),
               # '5': print_menu('food_menu'),
               # '6': print_menu('taxes_menu'),
               # '7': print('Этого раздела еще нет!'),
               # '8': print('Этого раздела еще нет!'),
               # '9': print_menu('end_menu')
              }'''


# print_menu(action_menu['2'])
# print_menu('build_menu')

# action_menu = {'print_main_menu': main_menu,
#  '1': 'Этого раздела еще нет!',
#  '2': print_menu,
#  '3': print_menu,
#  '4': print_menu,
#  '5': print_menu,
#  '6': print_menu,
#  '7': 'Этого раздела еще нет!',
#  '8': 'Этого раздела еще нет!',
#  '9': print_menu
# }
# action_menu['2']('build_menu')

class Farm:
  def __init__(self):
    self.count = 1
    self.money = 1000
    
class Market:
  def __init__(self):
    self.count = 1
    self.money = 1000

class Gold_player:
  def __init__(self):
    self.count = 1500

  def gold_minus(self,num):
    self.count -= num

  def gold_plus(self,num):
    self.count += num
    

def build_farm():
  """просит ввести кол-во ферм к постройке
     проверяет что кол-во * стоимсть< запаса золота
     запас золота игрока - стоимость постройки
     записать все изменения в хранилище"""

  #вызов ф-ии проверки золота
  #вызов ф-ии записи в хранилище
  print('Запустиласть функция постройки Фермы')

  bild_move()

def building_market():
  print('Запустиласть функция постройки Рынка')

  bild_move()
# @check_menu_number
def bild_move():
  print_menu("build_menu")
  
  num = input()

  action_build[num]()


def trade_move():
  print_menu("trade_menu")
  

def main_menu():
  print_menu('menu')
  num = input()

  return action_dict[num]()
  
action_dict = {
  '2': bild_move,
  '3': trade_move
}

action_build = {'1':build_farm,
                '2': building_market,
                '0': main_menu}


main_menu()

print('Ура, построено 10 ферм')
print_menu("build_menu")