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
    

  
    fLine = {"a" : 1, "b" : 2	}
    sLine = {"a" : 3, "b" : 4 }
    # dict1 = [fLine, sLine]
    # print(dict1)




 












































