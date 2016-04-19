#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random
import sys

__author__="andrew.tuley"
__date__ ="$01-Apr-2016 16:03:23$"


def generate_code():
    """

    :rtype: object
    """
    return int(random.random() * 9999)
    
    
if __name__ == "__main__":
    print("Crack the combination")
    overall = [0, 0, 0]
    loop = 0
    maxloop = 10000
    if len(sys.argv) > 1:
        maxloop = int(sys.argv[1])
        
    while loop < maxloop:
        print('Round {}'.format(loop))
        results = [0, 0, 0]
        code = generate_code()
        # method #1 start at 0000 and sequentially try to find it....
        # therefore the # of attempts will be code + 1
        results[0] = code+1

        # method #2 is to pick *unique* random numbers between 0000 and 9999 
        test = generate_code()
        attempts = 1
        values_tried = [False]*10000
        values_tried[test] = True
        while test != code:
            while values_tried[test]:
                test = generate_code()
            values_tried[test] = True
            attempts += 1
        results[1] = attempts

        # method #3 is to start at 0000 but jump in steps of 100
        # wrapping over 9999
        test = 0
        attempts = 1
        while test != code:
            test += 100
            if test > 9999:
                test -= 9999
            attempts += 1
        results[2] = attempts
        
        # locate the smallest # of attempts to solve
        winning_attempts = min(results)
        winners = []
        for method in range(3):
            if results[method] == winning_attempts:
                winners.append(method)
        # divide the prize among the winning methods
        try:
            prize = 1 / len(winners)
            for method in winners:
                overall[method] += prize
        except ZeroDivisionError:
            print('no winner')
        loop += 1
        
    for method in range(3):
        print('Method {0} succeeded {1} times ({2:.2%})'.format(method+1, overall[method], (overall[method]/maxloop)))