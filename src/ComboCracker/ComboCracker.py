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
    while loop < 10000:
        print ('Round {}'.format(loop));
        results = [0,0,0]; 
        code = generate_code();
        # method #1 start at 0000 and sequentially try to find it....
        # therefore the # of attempts will be code + 1
        results[0] = code+1;

        # method #2 is to pick *unique* random numbers between 0000 and 9999 
        test = generate_code();
        attempts=1;
        values_tried=[False]*10000;
        values_tried[test] = True
        while test != code:
            while values_tried[test]:
                test=generate_code();
            values_tried[test] = True;    
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
        
        winning_attempts = min(results);
        
        for method in 0,1,2:
            if results[method] == winning_attempts:
                overall[method] += 1;
        
        loop += 1
    print (overall);