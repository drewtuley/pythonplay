#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="andrew.tuley"
__date__ ="$01-Apr-2016 16:03:23$"

import random

def generate_code():
    code = random.random() * 9999;
    return int(code);
    
    
if __name__ == "__main__":
    print ("Crack the combination");
    overall=[0,0,0];
    loop = 0;
    while loop < 100:
        print ('Round {}'.format(loop));
        results = [0,0,0]; 
        code = generate_code();
        # method #1 start at 0000 and sequentially try to find it....
        # therefore the # of attempts will be code + 1
        results[0] = code+1;

        # method #2 is to pick random numbers between 0000 and 9999 
        test = generate_code();
        attempts=1;
        values_tried=[];
        values_tried.append(test);
        while test != code:
            while test in values_tried:
                test=generate_code();
            values_tried.append(test);    
            attempts += 1;
        results[1] = attempts;    

        # method #3 is start start at 0000 but jump in steps of 100
        # wrapping over 9999
        test = 0;
        attempts=1;
        while test != code:
            test += 100;
            if test > 9999:
                test -= 9999;
            attempts += 1;    
        results[2] = attempts;    
        winner = results.index(min(results));
        overall[winner] += 1;
        loop += 1
    print (overall);