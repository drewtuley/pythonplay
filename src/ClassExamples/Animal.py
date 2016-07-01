class Animal:

    def __init__(self):
        self.my_type = None

    def __eq__(self, other):
        return isinstance(other, Animal) and other.what() == self.my_type

    def show(self):
        print('I am a {}'.format(self.my_type))

    def make_noise(self):
        return None

    def what(self):
        return self.my_type