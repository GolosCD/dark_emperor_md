from object.game_text import *
import random as r
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

  def __str__(self):
    return f"{self.name}: {self.__count}"

  def get_current_count_builds(self):
    """Метод возвращает текущее кол-во построек"""

    return self.__count

  def get_current_price(self):
    """Метод возвращает стоимость одной постройки"""

    return self.__price

  def get_product_per_one(self):
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

    print(
        f'Максимальное кол-во построек, которое можно построить: {max_count}',
        '\n')


# Информер - игровая уведомлялка
class Informer:
  """Класс хранит реакции на различные игровые события"""

  def no_gold(self):
    print('Need more gold', '\n')
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
    print(welcome, '\n')
    input('Нажмите Enter для продолжения')
    print()

  def incorrect_key(self):
    """Метод печатается когда пользователь вбил несуществующий номер раздела меню"""

    print('Введите корректный пункт меню', '\n')
    input('Нажмите Enter для продолжения')
    print()


class Ration:
  """Данный класс отвечает за распределением еды для жителей королевства"""

  def __init__(self, json_ration: dict):
    self.__ration: dict = json_ration  # словарь хранит коэффициенты распределения еды
    self.__k_ration: float = json_ration.get('3')  #стартовое значение

  def get_k_ration(self):
    """Метод возращает текущий коэффициент распределения еды"""

    return self.__k_ration

  def set_k_ration(self, input_key: str):
    """Метод устанавливает новый коэффициент распределения еды"""

    self.__k_ration = self.__ration.get(input_key)

  def get_count_ration(self, count_villagers: int) -> int:
    """Метод возвращает кол-во еды которую сожрут жители в конце хода.
    Т.е эту еду надо списать со склада еды."""

    return int(count_villagers * self.get_k_ration())


class Taxes:
  """Данный класс отвечает за установку налогов"""

  def __init__(self, json_taxes: dict):
    self.__taxes: dict = json_taxes
    self.__k_taxes: float = json_taxes.get('3')

  def get_k_taxes(self):
    """Метод возвращает текущий коэффициент налогов"""

    return self.__k_taxes

  def set_k_taxes(self, input_key: str):
    """Метод устанавливает новый коэффициент налогов"""

    self.__k_taxes = self.__taxes.get(input_key)

  def get_count_taxes(self, count_villagers: int) -> int:
    """Метод возвращает кол-во налогов которое будет получено с жителей в конце года
    Т.е. столько надо будет прибавить в казну королевства"""

    return int(count_villagers * self.get_k_taxes())


# Класс для казны королвества (Произосится как Трежери)
class Resource:
  """Класс для хранения ресурсов королевства"""

  def __init__(self, name: str, count_default: int, price: int):
    self.name = name
    self.__count = count_default
    self.__price = price

  def get_count(self):
    """Метод возвращает текущее кол-во ресурса на складе"""

    return self.__count

  def add(self, qty: int):
    """Метод записывает указанное кол-во ресурсов на склад"""

    self.__count += qty

  def remove(self, qty: int):
    """Метод списывает указанное кол-во со склада"""

    if self.__count >= qty:  #если денег в казне хватает, то списываем
      self.__count -= qty
    else:
      self.__count = 0  #иначе 0

  def get_price(self):
    """Текущая цена ресурса"""

    return self.__price

  def set_price(self, price: int):
    """Метод изменяет цену ресурса"""

    self.__price = price


class Kingdom:
  """Класс для отображения количества жителей, золота и армии (сущности) в королевстве"""

  def __init__(self, count: int):
    self.__count = count

  def get_count(self):
    """Метод возвращает текущее кол-во сущности в королевстве"""
    return self.__count

  def add(self, amount: int):
    """Метод добавляющий количество сущности"""

    self.__count += amount

  def remove(self, amount: int):
    """Метод уменьшающий количество сущности"""

    if self.__count >= amount:
      self.__count -= amount
    else:
      self.__count = 0


class Year:
  """Класс для хранения параметров текущих года/хода/кона"""

  def __init__(self, start_year: int, end_year: int):
    #Стартовые параметры года для начала игры
    self.game_year = start_year
    self.end_year = end_year

  def add_year(self):
    """Метод увеличивает игровой год на один год"""

    self.game_year += 1

  def new_year(self):
    """Метод пересчитывает параметры нового года/хода/кона"""

    # добавляем один год
    self.add_year()


class Harvest:

  def __init__(self, harvest_key: str, harvest_interval: dict,
               price_modificator: dict):
    self.__harvest_key = harvest_key
    self.__harvest_interval = harvest_interval
    self.__harvest_ratio = 1.0
    self.__price_modificator = price_modificator

  def get_ratio(self) -> float:
    """Метод возвращает коэффициент урожая"""

    return self.__harvest_ratio

  def get_price_modificator(self) -> float:
    """Метод возвращает коэффициент цены"""
    
    return self.__price_modificator.get(self.__harvest_key)

  def calc_harvest_ratio(self):
    """Метод пересчитывает урожайность"""

    # тип урожая
    harvest_type = ['low', 'average', 'hight']

    # качество урожая
    harvest_quality = ['poor', 'average', 'good']

    # выбираем случайный тип урожая и качество урожая
    self.__harvest_key = r.choice(harvest_type)\
      + '_' + r.choice(harvest_quality)

    self.__harvest_ratio = r.uniform(*(self.__harvest_interval.get(self.__harvest_key))) * 100
    
class Price:
  """Класс для хранения цен на ресурсы"""

  def __init__(self, dict_price_sale: dict):
    self.__price_food = dict_price_sale.get('food')
    self.__price_iron_ore = dict_price_sale.get('iron_ore')
    self.__price_weapon = dict_price_sale.get('weapon')

  def get_price_food(self):

    return self.__price_food

  def get_price_iron_ore(self):

    return self.__price_iron_ore

  def get_price_weapon(self):

    return self.__price_weapon


  def cal_price_food(self, harvest: Harvest):
    """Метод рассчитывает цену за ед. еды"""

    min_harvest = 20  # минимальная урожайность
    max_harvest = 170  # максимальная урожайность
    max_price = 100  # максимальная цена
    min_price = 20  # минимальная цена
    koef_harvest = (min_harvest - max_price) / (max_harvest - min_price)
    free_member = max_price + (koef_harvest * -1 * min_price)
    first_price = (harvest.get_ratio() * koef_harvest) + free_member
    result_price = round(first_price * (1 - harvest.get_price_modificator()))
    
    self.__price_food = result_price
    
    