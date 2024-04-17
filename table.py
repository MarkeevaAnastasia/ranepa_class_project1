#Cоздание класса таблицы
import pandas
import csv

table1 = pandas.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8]})
print(table1)
table1.to_csv("table1.csv")
with open("table.csv", "w") as file:
  file = csv.DictWriter()






class Table:
  def __init__(self, columns = None):
    self.columns = columns or []
    self.rows = []

  def add_row(self, row):
    

  
     
  
    #print(2 + 2)

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

    #BMW = Car()
    #BMW.color = "White"

    #Matis = Car()
    #Matis.color = "Red"

    #Какой класс явялется шаблоном для экземпляра?
    #print(BMW.__class__)

    #Вызов метода
    #Также, как мы вызывали для lst, str, int, float, dict, set, tuple

    #BMW.sound()   #ошибка

    #метод может повлиять на характеристика других объектов или самого себя
    #для кого будет происходить изменение не указано

    #print(BMW.sound())
    #print(BMW.start_engine(key="Ключ от авто"))

    #ИТОГ
    # 1. Классы и экземпляры-объекты
    # 2. Атрибуты и методы
    # 3. Связанные методы и аргумент self
    # 4. Магические методы (__init__)



    #Cоздание класса таблицы
    #import pandas
    #import csv

    # table1 = pandas.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8]})
    # print(table1)
    # table1.to_csv("table1.csv")
    # with open("table.csv", "r") as file:
    #   file = csv.DictWriter()









    fLine = {"a" : 1, "b" : 2	}
    sLine = {"a" : 3, "b" : 4 }
    # dict1 = [fLine, sLine]
    # print(dict1)



table1 = pandas.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8]})
print(table1)
table1.to_csv("table1.csv")
with open("table.csv", "w") as file:
  file = csv.DictWriter()


class Table:
  def __init__(self, columns = None):
    self.columns = columns or []
    self.rows = []

  def add_row(self, row):
    if not self.columns:
        self.columns = [{key: value} for key, value in row.items()]
    else:
        for column in self.columns:
            for key, value in row.items(): 
                column[key] = value
  def __bool__(self):
    return bool(self.columns)
  def __str__(self): 
    if not self.columns:      
      return ""
table = Table()
fLine = {"a": 2, "b": 4}
sLine = {"a": 3, "b": 9}
table.add_row(fLine)
print(table.columns)
table.add_row(sLine)
print(table.columns)
print(table)




table1 = pandas.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8]})
print(table1)
table1.to_csv("table1.csv")
with open("table.csv", "w") as file:
  file = csv.DictWriter()

def __init__(self, columns=None):
   self.columns = columns or []

def add_row(self, row):
   if not self.columns:
       self.columns = [{key: value} for key, value in row.items()]
   else:
       for column in self.columns:
           for key, value in row.items():
               column[key] = value

def __bool__(self):
   return bool(self.columns)
def __str__(self):
   if not self.columns:
       return ""

   keys = set()
   for column in self.columns:
       keys.update(column.keys())

   header = " ".join(str(key) for key in keys)

   lines = [header]
   for column in self.columns:
       line = " ".join(str(column.get(key, "")) for key in keys)
       lines.append(line)

   return "\n".join(lines)


















































