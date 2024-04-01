print(2 + 2)

#Первый пробный класс
#Этап создания класса
#Класс - шаблон, по которому будут создаваться объекты

class Car:
   #метод __init__ - конструктор класса
   #внутрь __init__ можно передавать аргументы
  def __init__(self, color, wheels, helm):
    #атрибуты - переменные внутри класса
    self.helm = helm
    self.color = "Black"
    self.wheels = 4
    self.engine_status = False

  
  #методы - функции внутри класса
  def sound(self):
    return "Bebebe"

  #нужно указывать какие атлибуты будут меняться
  #self.engine_status
  def start_engine(self, key):
    if key == "Ключ от авто":
      engine_status = True
      return f"статус машины: {engine_status}"
    else:
      return "требуется ключ"


#Этап создания объекта класса
#экземпляр класса, который живет своей жизнью

BMW = Car()
BMW.color = "White"

Matis = Car()
Matis.color = "Red"

#Какой класс явялется шаблоном для экземпляра?
print(BMW.__class__)

#Вызов метода
#Также, как мы вызывали для lst, str, int, float, dict, set, tuple

#BMW.sound()   #ошибка

#метод может повлиять на характеристика других объектов или самого себя
#для кого будет происходить изменение не указано

print(BMW.sound())
print(BMW.start_engine(key="Ключ от авто"))

#ИТОГ
# 1. Классы и экземпляры-объекты
# 2. Атрибуты и методы
# 3. Связанные методы и аргумент self
# 4. Магические методы (__init__)
#
#
#
#
#
#









