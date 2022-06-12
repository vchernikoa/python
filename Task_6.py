'''
Есть класс Animal c одним методом voice().
class Animal:
def voice(self):
pass
1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().
'''

class Animal:
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

Mysay.voice()
Sharik.voice()
Py.voice()