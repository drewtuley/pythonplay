from src.ClassExamples.Animal import Animal
from src.ClassExamples.Cat import Cat
from src.ClassExamples.Dog import Dog
from src.ClassExamples.Feline import Feline


def is_or_isnot(state):
    if state:
        return 'is'
    else:
        return 'is not'


def animal_speak(animal):
    print('I am a {} and I go {}'.format(animal.what(), animal.make_noise()))


c = Cat()
animal_speak(c)

d = Dog()
animal_speak(d)

print('Cat {} subclass of Feline'.format(is_or_isnot(issubclass(Cat, Feline))))
print('Cat {} instance of Feline'.format(is_or_isnot(isinstance(c, Cat))))
print('Cat {} instance of Dog'.format(is_or_isnot(isinstance(c, Dog))))
print('Cat {} instance of Animal'.format(is_or_isnot(isinstance(c, Animal))))

print(d.make_noise())
print(c.make_noise())

c1 = Cat()
c2 = Cat()
if c1.__eq__(c2):
    print('{} = {}'.format(c1.what(), c2.what()))
