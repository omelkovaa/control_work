class Product():
    def __init__(self, name, magazin, price):
        self.__name = name
        self.__magazin = magazin
        self.__price = price
        self.arr = []

    def add_elem(self):
        self.arr.append(self.__name, self.__magazin, self.__price)

    def info(self, arr):
        for i in range(arr):
            print(arr[i])

    def infouser(self):
        a = input()
        if a == self.__name:
            print(self.__name, self.__magazin, self.__price)

    def __add__(self, priceAll):
        priceAll += self.__price
        return priceAll


class Stock():
    def __init__(self):
        self._Product = Product()

    def arr(self, elem):
        self._Product.arr.append(elem)

product = Product('ff', 'gg', 120)
print(Product)
product = Product1('gg','mm', 150)

    def __add__(Product, Product1):
        return price (product + priceproduct1)

