#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:53:29 2024

@author: wesleychapman
Lab 3
"""

import os
import statistics


def sum_distinct(lst):
    for i in range(len(lst)):
        lst[i] = sum(set(lst[i]))
    return lst



def generate_files(files, direct):
    
    if os.path.exists(direct):
        pass
    else:

        os.makedirs(direct)
        
        for file in files:
            with open(direct + "/" + file, "w") as outfile:
                outfile.write(file.rstrip(".txt").rstrip(".csv"))
        


def clean_means(tup):
    mean_lst = []
    for row in tup:
        int_row = []
        for item in row:
            if isinstance(item, int):
                int_row.append(item)
        print(int_row)
        mean_lst.append(statistics.mean(int_row))
        
    return mean_lst
        
    
    
    




def main():
    
    # Q1
    print(sum_distinct([(1, 1, 2), (3, 5, 6, 5)]))
    
    # Q2
    generate_files(["hello.txt", "bye.txt"], "mydir")
    
    # Q4
    print(clean_means(((1, 2, 3), (1, "", 3), ("", 2, 3))))
    
if __name__ == "__main__":
    main()

