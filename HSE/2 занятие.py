class Cat:
    def __init__(self, myau_sound, color, age, poroda):
        self._myau_sound = myau_sound
        self._color = color
        self._age = age         #обычная
        self._poroda = poroda #приватная __

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if self._age > new_age:
            return
        self._age = new_age

    def say_myau(self):
        print(self._myau_sound)


class HouseCat(Cat):    #наследование
    def __init__(self, name, owner, myau_sound, color, age, poroda):
        self._name = name
        self._owner = owner

    def owner(self):
        return self._owner

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if self._age > new_age:
            return
        self._age = new_age
    def say_myau(self):
        self._myau_sound

    def owner(self):
        return self._owner

cat1 = Cat("Мяууууу", "Черный", 6, "Британская")
#ИНКАПСУЛЯЦИЯ - ВСЕ ЧТО ВНУТРИ КЛАССА ОСТАЕТСЯ ВНУТРИ КЛАССА

cat1.say_myau()
print(cat1._poroda)

def describe_cat(cat):
    print("Возраст: ", cat.age)
    print("Кошка мyрчит так: ", end="\n") # что выводиться в конце строки
    cat.say_myau()

cat2 = HouseCat("Мурка", "Георгий","Мяууу", "Черная", 6, "Британская")
cat3 = Cat("Мааааа", "Черная", "15", "Британская")

describe_cat(cat2)
cat2.age = 4
describe_cat(cat3)
cat2.age = 22
describe_cat(cat2)
cat2.age = 8
from dataclasses import dataclass

