"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики
"""

from task1 import Mammals, Birds, Fishes


class Factory:

    def __init__(self, animal_class, **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'kind':
                self.kind = value
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'breed':
                self.breed = value
            if key == 'size':
                self.size = value

    def get_info(self):
        if self.animal_class == 'bird':
            return Birds(self.kind, self.name, self.age, self.color)
        elif self.animal_class == 'mammal':
            return Mammals(self.kind, self.name, self.age, self.breed)
        elif self.animal_class == 'fish':
            return Fishes(self.kind, self.name, self.age, self.size)


if __name__ == '__main__':
    animal1 = Factory(animal_class='bird', kind='Попугай', name='Кеша', age=1, color='голубой')
    print(animal1.get_info().get_animal_info())

    animal2 = Factory(animal_class='mammal', kind='Кот', name='Оскар', age=3, breed='Девон-рекс')
    print(animal2.get_info().get_animal_info())

    animal3 = Factory(animal_class='fish', kind='Дельфин', name='Шустрый', age=2, size='3 м')
    print(animal3.get_info().get_animal_info())