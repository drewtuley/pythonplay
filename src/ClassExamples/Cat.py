from src.ClassExamples.Feline import Feline


class Cat(Feline):
    def __init__(self):
        self.my_type = 'Cat'

    def make_noise(self):
        return 'Meow'