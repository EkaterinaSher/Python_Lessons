#задание_1
a = [[1,1,1], [2,2,2], [3,3,3]]
b = [[4,4,4], [5,5,5], [6,6,6]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self,other):
        d = []
        for i in range(len(self.lists)):
            d.append([])
            for j in range(len(self.lists[i])):
                d[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, d))

print(Matrix(a))
print(Matrix(b))
print(Matrix(a) + Matrix(b))

#задание_2

class Wears:
    def __init__(self, name, tissue_volume):
        self.name = name
        self.tissue_volume = tissue_volume

    def __add__(self, other):
        return self.tissue_volume + other.tissue_volume



class Coat(Wears):
    def __init__(self, size):
        self.size = size

    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 34:
            self.__size = 34
        elif size > 58:
            self.__size = 58
        else:
            self.__size = size

    def tissue_volume(self):
        return self.size/6.5 + 0.5


class Suit(Wears):
    def __init__(self, hight):
        self.hight = hight

    @property
    def hight(self):
        return self.__hight

    @hight.setter
    def hight(self, hight):
        if hight < 140:
            self.__hight = 140
        elif hight > 205:
            self.__hight = 205
        else:
            self.__hight = hight

    def tissue_volume(self):
        return 2 * self.hight + 0.3
    


coat1 = Coat(44)
print(coat1.size)
print(coat1.tissue_volume())
suit1 = Suit(180)
print(suit1.hight)
print(suit1.tissue_volume())
print(coat1.tissue_volume() + suit1.tissue_volume())

#задание_3

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity
        

    def __sub__(self, other):
        return self.quantity - other.quantity
    

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity


    def make_order (rows, asterisks):
        return '\n'.join(['*' * rows for _ in range(asterisks // rows)]) + '\n' + '*' * (asterisks % rows)


cell1 = Cell(44)
cell2 = Cell(78)
print(cell1.__add__(cell2))
print(cell1.__sub__(cell2))
print(cell1.__mul__(cell2))
print(cell1.__truediv__(cell2))
a = Cell.make_order(17,54)
print(a)


