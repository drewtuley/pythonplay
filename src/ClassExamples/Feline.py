from src.ClassExamples.Animal import Animal


class Feline(Animal):
    def __init__(self):
        self.my_type = 'Feline'

    def make_noise(self):
        return 'Purr'
