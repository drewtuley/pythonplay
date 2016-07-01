from src.ClassExamples.Animal import Animal


class Canine(Animal):
    def __init__(self):
        self.my_type = 'Canine'

    def make_noise(self):
        return 'Woof'
