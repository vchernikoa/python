'''
Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали
статический метод родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.
'''

class Animal:
    count = 0
    def __init__(self):
        Animal.count = Animal.count + 1

    def printCount():
        print(Animal.count)

    printCount= staticmethod(printCount)

    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print("May")

class Dog(Animal):
    def voice(self):
        print("Gav")

class Snake(Animal):
    def voice(self):
        print("Shhhh")

Mysay = Cat()
Sharik = Dog()
Py = Snake()

Animal.printCount()