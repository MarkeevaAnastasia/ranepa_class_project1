import pandas
import csv

table1 = pandas.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8]})
print(table1)
table1.to_csv("table1.csv")
with open("table.csv", "w") as file:
  pass


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








