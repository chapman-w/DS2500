#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:52:10 2024

@author: wesleychapman
Lab 1
NUID: 002861490

"""


numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



def lst_to_dct(data_lst):
    
    data_dct = {}
    for row in (data_lst):
        data_dct[row[0]] = row[1:]
        
    return data_dct



def col_to_lst(data_lst, col):
   n_lst = []
   for row in data_lst:
       n_lst.append(row[col])
   return n_lst



def sum_cols(data_lst):
    l_lst = []
    for row in range(len(data_lst[0])):
        l_lst.append(sum(col_to_lst(data_lst, row)))
    return l_lst
        
    




def main():
    
    print(lst_to_dct(numbers))
    
    
    print(col_to_lst(numbers, 2))


    print(sum_cols(numbers))
    
    
if __name__ == "__main__":
    main()