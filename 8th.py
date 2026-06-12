from dataclasses import dataclass

#N1

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("can't withdraw more than your balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

#N2 ----------------------------------------------------

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return len(self.items) == len(other.items)


cart1=ShoppingCart(["marwyvi", "cola", "ludi", "yava"])
cart2=ShoppingCart(["wigni", "rveuli", "wyali"])
cart3=ShoppingCart(["mawoni", "rdze", "xorci", "nutella"])

print(cart1==cart2)
print(cart2==cart3)
print(cart1==cart3)

#N3 ---------------------------------------------------------

@dataclass
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_classic(self):
        return self.year<1970

book1=Book("return of the king", "Jrr tolkien", 1954)
book2=Book("moby dick", "herman melville", 1851)
book3=Book("blood meridian", "cormac mccarthy", 1985)
book4=Book("red rising", "pierce brown", 2014)

print(book1.is_classic())
print(book2.is_classic())
print(book3.is_classic())
print(book4.is_classic())

#N4 ------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("person removed")

me=Person("saba")
print(me)
del me

#N5 --------------------------------------------------

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.__celsius * (9 / 5) + 32

temp=Temperature(25)
print(temp.celsius)
print(temp.fahrenheit)

#N6 --------------------------------------------------

class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __iter__(self):
        return iter(self.items)

mine=CustomList([1,2,3,10,47])
print(mine.items)
print("---------")
print(mine.items[0])
print("---------")
for i in mine.items:
    print(i)

#N7 ----------------------------------

class Refrigerator:
    def __init__(self, items: list):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"fridge with {len(self.items)} items"

    def __del__(self):
        print("fridge unplugged!")

cart = Refrigerator(["milk"])
print("milk" in cart)
print(cart.items)
del cart

#N8 --------------------------------------

class FunnyCalculator:
    def __add__(self, other):
        print("Why are you adding numbers? Just buy a calculator")

    def __mul__(self, other):
        print("Multiplication is too mainstream...")

    def __truediv__(self, other):
        if other==0:
            print("ZeroDivisionError? Nah, let’s just say infinity")
        else:
            print("Division is too mainstream...")

    def __str__(self):
        print("I’m the funniest calculator in Python!")

calc = FunnyCalculator()
print(calc+5)
print(calc*5)
print(calc/0)