from object.game_text import *

"""Модуль хранит независимые классы для игры
Классы содержат методы в основном они делятся на три категории:
 get_ - методы что-то возращают;
 set_ - методы что-то меняют;
 print_ - методы что-то печатают;
 add_ методы что-то добавляют;
 revome_ - методы что-то уменьшают;
"""

# Класс "Здание" - для управления зданиями в игре
class Build:
  """Класс для хранения информации о постройке"""
  
  def __init__(self, name: str, count: int, price: int, product_per_one: int):
    self.name = name
    self.__count = count
    self.__price = price
    self.__product_per_one = product_per_one

  def get_current_count_builds(self):
    """Метод возвращает текущее кол-во построек"""
    
    return self.__count

  def get_current_price (self):
    """Метод возвращает стоимость одной постройки"""

    return self.__price

  def get_product_per_one (self):
    """Метод кол-во продуктов производимых одной постройкой"""

    return self.__product_per_one

  def add_count_build(self, count: int):
    """Метод увеличивает кол-во построек"""
    
    self.__count += count

  def remove_count_build(self, count: int):
    """Метод уменьшает кол-во построек"""
    
    self.__count -= count

  def print_max_count(self, gold_in_treasury: int):
    """Метод печатает максимальное кол-во построек, которое можно построить"""
    
    max_count = gold_in_treasury // self.get_current_price()
    
    print(f'Максимальное кол-во построек, которое можно построить: {max_count}','\n')


# Класс для казны королвества (Произосится как Трежери)
class Treasury:
  """Казна королевства"""
  
  def __init__ (self,gold_default: int):
    self.__gold = gold_default
    
  def get_current_gold(self):
    """Метод возвращает текущее кол-во золота в казне королевства"""
    
    return self.__gold

  def add_gold(self, price: int):
    """Метод записывает указанную сумму в казну королевства"""

    self.__gold += price

  def remove_gold(self, price: int):
    """Метод списывает указанную сумму из казны королевства"""
    
    self.__gold -= price


# Информер - игровая уведомлялка
class Informer:  
  """Класс хранит реакции на различные игровые события"""

  def no_gold(self):
    print('Need more gold','\n')
    input('Нажмите Enter для продолжения...')
    print()


# Принтер - печатает разные вещи
class Printer:
  """Класс для печати игровых меню и текста"""
  
  def __init__(self, json_menu: dict):
    self.__menu_objects = json_menu

  def menu(self, name: str):
    """Метод печатает меню"""

    for num, name_line in self.__menu_objects.get(name).items():
      print(f'{num} - {name_line}')
    print()

  def welcome(self):
    """Метод печатает приветственное сообщение"""
    print(welcome,'\n')
    input('Нажмите Enter для продолжения')
    print()

  def incorrect_key(self):
    """Метод печатается когда пользователь вбил несуществующий номер раздела меню"""
    
    print('Введите корректный пункт меню','\n')
    input('Нажмите Enter для продолжения')
    print()