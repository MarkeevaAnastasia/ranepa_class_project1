import pandas

# необходимый модуль
import csv

class Table:
    def __init__(self, columns=None):
        self.columns = columns or []
        self.rows = []

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            r = csv.DictReader(file)
            self.columns = r.fieldnames
            for row in r:
                self.add_row(row)

    def load_from_dicts(self, *dicts):
        for d in dicts:
            self.add_row(d)

    def add_row(self, row):
        if not self.columns:
            self.columns = list(row.keys())
        self.rows.append(row)

    def bool(self):
        return bool(self.rows)

    def __str__(self):
        col_str = ' '.join(self.columns)
        rows_str_list = []

        for row in self.rows:
            row_arr = []

            for col in self.columns:
                value = str(row[col])
                row_arr.append(value)

            row_str = ' '.join(row_arr)
            rows_str_list.append(row_str)

        rows_str = '\n'.join(rows_str_list)

        return col_str + "\n" + rows_str

table = Table(['a', 'b'])
fLine = {"a": 2, "b": 4}
sLine = {"a": 3, "b": 9}

table.add_row(fLine)
table.add_row(sLine)
print(table)

print()

table_from_file = Table()
table_from_file.load_from_file("table.csv")
print(table_from_file)



























