#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="andrew.tuley"
__date__ ="$09-Mar-2016 13:25:39$"

from random import choice, seed;

doors = [];
win=1;
lose=2;

def setup_doors():
    #print('doors to automatic');
    while doors.count(win) <1: 
        doors.append(win);
    while doors.count(lose) <2: 
        doors.append(lose);
    #sprint(doors);
    
def play(tries, change):
    wins=0;
    loop=0;
    while loop < tries:
        setup_doors();
        door = choice(doors);
        #print ('I picked door {}'.format(door));
        doors.remove(lose);

        if change:
            #print ('i shall change');
            door = choice(doors);
        if door == win:
            wins += 1;
        loop += 1;    
    print ('I won {0} times by {1}'.format(wins, 'changing' if change else 'not changing' ));    

if __name__ == "__main__":
    seed();
    
    play(100000,True);
    play(100000,False);
