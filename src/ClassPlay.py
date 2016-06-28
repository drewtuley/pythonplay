#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrew.tuley"
__date__ = "$07-May-2015 13:08:14$"


class Play:
    classvar = 0

    def __init__(self, inst):
        self.inst = inst;

    def show(self):
        print('Inst=' + str(self.inst) + ' classvar=' + str(self.classvar));

    @classmethod
    def add(cls, add):
        cls.classvar += add

    def mult(self, a, b):
        while a > 0:
            self.add(b)
            a -= 1


if __name__ == "__main__":
    p1 = Play(1)
    p2 = Play(2)

    p1.show()
    p2.show()
    Play.add(2)
    p2.show()
    p1.add(10)
    p1.show()
    p2.show()
    p2.add(-12)
    p1.show()
    p2.show()
    p2.mult(2, 3)
    p1.show()
    p2.show()
