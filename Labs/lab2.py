#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:51:04 2024

@author: wesleychapman
Lab 2
NUID: 002861490
"""


import csv
import matplotlib.pyplot as plt 
import statistics

FILENAME = "speed_restrictions-1.csv"
R_SPEED_COL = 'Restriction_Speed_MPH'
LINE_COL = "Line"
PRIORITY_COL = "Priority"
DIST_COL = "Restriction_Distance_Feet"

def read_file(filename):
    '''Reads the CSV file and returns
    a list of lists.'''
    data = [] 
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data

def lst_to_dct(lst):
    ''' Converts a list of list to a
    dictionary of lists, where the key is
    the column name. This time, the list of 
    lists has the header row as well.
    '''
    # TODO: CODE WALK
    # OK WHAT DOES THIS CODE DO?!
    dct = {}
    num_of_cols = len(lst[0])
    for i in range(num_of_cols):
        # going through the top row (headers)
        # and creates a key in the dictionary
        header = lst[0][i] 
        dct[header] = [] 
        # going down the rows
        # adding to that one column
        for row in lst[1:]:
            dct[header].append(row[i])            
    return dct
    
def clean_mph(lst):
    '''Returns a new list which is int for 
    the "X mph" column'''
    new_lst = []
    for item in lst:
        new_lst.append(int(item.split()[0]))
    return new_lst



def choose(dct, header1, header2, cond1):
    ''' returns a list from dct based on condition from other list
    ie: total_track_miles of all green line trains
    (numpy.where)
    '''
    newlst = []
    for i in range(len(dct[header1])):
        if dct[header1][i] == cond1:
            newlst.append(dct[header2][i])
    return newlst
    
        
def str_to_int(lst):
    int_lst = []
    for i in lst:
        int_lst.append(int(i))
    return int_lst




def main():
   
    data_lst = read_file(FILENAME)
    data_dct = lst_to_dct(data_lst)
    print(data_dct)
    
    
    
    # clean the speed mph column
    data_dct[R_SPEED_COL] = clean_mph(data_dct[R_SPEED_COL])
    print(data_dct[R_SPEED_COL])
    
    # Q1 avg speed restriction
    avg_speed_restriction = statistics.mean(data_dct[R_SPEED_COL])
    print(f"Average speed restriction is {round(avg_speed_restriction, 2)} mph.")
    
    # Q2 most common line with a restriction
    line = statistics.mode(data_dct[LINE_COL])
    print(f"Line with most restrictions is {line}.")
    
    
    
    # LAB2 Q's
    
    # Q1: What is the median restricted speed on orange line?
    print(statistics.median(choose(data_dct, 'Line', 'Restriction_Speed_MPH', 'Orange Line')))
    
    
    # Q2: Which line has the most total feet of track under speed restrictions? 
   
    OrangeLine = sum(str_to_int((choose(data_dct, 'Line','Restriction_Distance_Feet', 'Orange Line'))))
    print(f"Sum of Orange Line is {OrangeLine}.")
    
    GreenLine = sum(str_to_int((choose(data_dct, 'Line', 'Restriction_Distance_Feet', 'Green Line'))))
    print(f"Sum of Green Line is {GreenLine}.")
    
    MattapanLine = sum(str_to_int((choose(data_dct, 'Line', 'Restriction_Distance_Feet', 'Mattapan Line'))))
    print(f"Sum of Mattapan Line is {MattapanLine}.")
    
    RedLine = sum(str_to_int((choose(data_dct, 'Line', 'Restriction_Distance_Feet', 'Red Line'))))
    print(f"Sum of Red Line is {RedLine}.")
    
    
    # Q3: What is the second-most common reason for a speed restriction? 
    print(statistics.mode(data_dct['Restriction_Reason']))
    new_data = data_dct['Restriction_Reason']
    print(new_data)
   
    # print(statistics.mode(new_data['Restriction_Reason']))
    
    
    
    


if __name__ == "__main__":
    main()

