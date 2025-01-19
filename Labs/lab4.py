#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:01:12 2024

@author: wesleychapman
Lab 4
"""

import statistics


TEST = [10, 30, 40, 50, 20, 30, 10]


def str_to_int(lst):
    ''' returns a list of ints
    '''
    return [int(item) for item in lst]


def variance(lst, mode='sample'):
    for i in lst:
        if mode == 'population':
            variance = round(statistics.pvariance(lst), 2)
        else:
            variance = round(statistics.variance(lst), 2)
            
    return variance
        

    
def z_score(lst):
    
    newlst = []
    for i in lst:
        newlst.append((i - statistics.mean(lst)) / statistics.stdev(lst))
    return newlst
    
    
    
def quartiles(lst):
   
    return tuple(str_to_int(statistics.quantiles(lst, n = 4)))
                  
    
    
    
    
    
def main():
    
    print(variance(TEST))
    print(variance(TEST, 'population'))
        
    print(str_to_int(z_score([2, 4, 6])))
    
    print(quartiles([4, 5, 6]))
    
    
if __name__ == "__main__":
    main()    
    