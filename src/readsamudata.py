import numpy as np
from tabulate import tabulate
from __format import format_element
import statistics as stat

class ReadSamuData:
    """
    Samu Data
    =========

    That's the main class of Samu Data
    
    """
    def __init__(self, path):
        self.__path = path
        self.data = self.datas()

        if not self.__path.endswith(".smdt"):
            raise ValueError("Esse não é o path certo")

    @property
    def columnlen(self):
        columnLen = len(self.columns)
        return columnLen
    
    
    @property
    def columns(self):
        the_file = self.__readFile()
        columns = the_file[0].split(";")
        return columns

    #The info will base on the second row
    def info(self):
        the_file = self.__readFile()
        secondrow = the_file[1].split(";")
        text = f"{self.columns}\n{[i for i in secondrow]}"
        return text




    def sizerows(self, withoutcolnames=True):
        the_file = self.__readFile()
        count = 0
        for row in the_file:
            count += 1

        if withoutcolnames:
            return count - 1
        else:
            return count
        



    def show(self, head=None, tail=None):
        if head:
            return self.__head(head=head)
        
        elif tail:
            return self.__tail(tail=tail)
        
        else:
            return self.__head()



    def __head(self, head=5):
        the_file = self.__readFile()
        text = [row.split(";") for row in the_file[1:head+1]]
        return tabulate(text, tablefmt="pipe", headers=the_file[0].split(";"))

    # Need more implamentation...
    def __tail(self, tail=5):
        the_file = self.__readFile()
        text = [row.split(";") for row in the_file[-1:-(tail+1)]]
        return tabulate(text, tablefmt="pipe", headers=the_file[0].split(";"))



    def __readFile(self):
        with open(self.__path, "r") as file:
            content = file.read().strip().split("\n")
        
        return content
    
    def datas(self):
        the_file = self.__readFile()
        new_list = []
        for row in the_file:
            new_list.append(format_element(row.split(";")))

        return new_list
    
    def __repr__(self):
        rows = [str(row) for row in self.data]
        return f"ReadAF(\n{"\n".join(rows)})"

    @property
    def indexrow(self):
        return self.data[1:]
    
    @property
    def indexcol(self):
        """
        That's gonna return the column specified base on the index
        ["Name", "Age", "Salary"]
        ["John", "34", 5600]
        ["Marry", 56, 9392]
        >>> indexcol[0] # it gonna return the ('Jonh', 'Marry')
        """
        return list(zip(*self.data[1:]))
    
    
    def mean(self, column):
        #Take the index of the column
        index_column = self.columns.index(column)
        # Use indexcol property to return the column base on the index of the specific column
        column = self.indexcol[index_column]
        return stat.mean(column)