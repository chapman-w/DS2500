#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 00:14:18 2024

@author: wesleychapman
NUID: 002861490
Homework 1
"""

import csv
import matplotlib.pyplot as plt 
import statistics

TOTAL_LOANS = "total_loans_per_state.csv"
BORROWERS = "num_borrowers_per_state.csv"



def str_to_float(data_item):
    '''converts a string to a float
    '''
    cleaned_str = data_item.replace(",", "").replace("$", "")
    return float(cleaned_str)



def read_file(filename):
    '''Reads the CSV file and returns
    a list of lists.'''
    data = [] 
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data



def lst_to_dct2(lst):
    ''' takes a list of lists and converts to dictionary
    uses the index 0 from each list as the key
    '''
    ndct = {}
    for row in lst:
        ndct[row[0]] = row[1:]
        
    return ndct
    


def clean_data(data_lst):
    ''' goes through list of lists
    and cleans the numeric parts
    Keep the first item, convert the rest to float ONLY
    if it is not a blank string.
    '''
    cleaned_lst = []
    for row in data_lst:
        cleaned_row = []
        # add the state name
        cleaned_row.append(row[0])
        cleaned_lst.append(cleaned_row)
        # go through remaining data in the row
        # skip the first item
        for i in range(1, len(row)):
            if len(row[i]) > 0:
                cleaned_row.append(str_to_float(row[i]))
              
    return cleaned_lst



def column(dct, index):
    ''' iterates by index over a dictionary of lists
    to create a new list based off the values from the
    given index
    '''
    newlst = []
    for key in dct:
           newlst.append(dct[key][index])
        
    return newlst



def rows_avgd(dct):
    ''' takes a dct of lists with numeric values and returns
    a new list with the averaged value for each key in the dct 
    '''
    avgd_dct = {}
    # iterate over each key in dictionary
    for key in dct:
    # assign new state keys to their corresponding mean values
        avgd_dct[key] = statistics.mean(dct[key])
        
    return avgd_dct
        


def chg_by_year(dct, key):
    ''' takes a dct of lists, calls a certain list
    based on key, calculates the change from item 
    to item in the list, appends those values to new list.
    '''
    values = dct[key]
    changes = []
    for i in range(1, len(values)):
        change = abs(values[i] - values[i-1])
       
        changes.append(change)
        
    return changes



def key_from_value(dct, value):
    ''' takes in a value from a dictionary and returns the corresponding key
    '''
    # i is the key, x is the value in dct
    for i, x in dct.items():
        if x == value:
            return i
        


def plot_hist(dct1, dct2):
    ''' plot the average outstanding balance 
    per borrower in each state, in 2021
    '''
    
    # Total loans per state
    tot_loans = column(dct1, 6)
    # Total borrowers per state
    tot_borrow = column(dct2, 6)
    # Average outstanding balance per borrower
    avg_outstanding = conv_to_millions(div_lsts(tot_loans, tot_borrow))
   
    # Prepare the plot
    plt.title("Average Outstanding Balance\
 Per Borrower in Each State in 2021")
    plt.xlabel("Average Outstanding Balance per Borrower ($)")
    plt.ylabel("# of States")
    
    # Plot the data
    plt.hist(avg_outstanding, bins=[25000, 30000, 35000, 40000, 
                                    45000, 50000, 55000,
                                    60000], color='forestgreen')
    
    # Show the plot
    plt.show()



def plot_line(dct1, dct2):
    ''' plot how the average outstanding balance 
    per borrower changed over time between 
    Minnesota and Massachusetts
    '''
    
    time = [2016, 2017, 2018, 2019, 2020, 2020, 2021]
    # Minnesota loans
    mn_loans = dct1['Minnesota']
    # Minnesota borrowers
    mn_borrowers = dct2['Minnesota']
    # Massachusetts loans
    ma_loans = dct1['Massachusetts']
    # Massachusetts borrowers
    ma_borrowers = dct2['Massachusetts']
    
    # Minnesota average outstanding balance per borrower over time
    mn_outbal = conv_to_millions(div_lsts(mn_loans, mn_borrowers))
    # Massachusetts average outstanding balance per borrower over time
    ma_outbal = conv_to_millions(div_lsts(ma_loans, ma_borrowers))
   
    # Prepare the plot
    plt.title("MN & MA Avg Outstanding Balance per Borrower (2016-2021)")
    plt.xlabel("Year")
    plt.ylabel("Avg Outstanding Balance per Borrower ($)")
    
    # Plot the data
    plt.plot(time, mn_outbal, label='Minnesota', color='blue')
    plt.plot(time, ma_outbal, label='Massachusetts', color='red')
    plt.legend()
    
    # Show the plot
    plt.show()
    


def div_lsts(lst1, lst2):
    ''' takes in two lists of equal length
    and divides lst1 by lst2, putting the 
    corresponding values into a new list.
    '''
    result = []
    # goes through each index of lst1 and divides it by corresponding
    # index in lst2
    for i in range(len(lst1)):
        result.append(lst1[i] / lst2[i])
            
    return result



def conv_to_millions(lst):
    ''' takes list from total loans data and converts to correct
    $ amount in millions
    '''
    mil = []
    for i in lst:
        mil.append(i*1000000)
        
    return mil



def main():

    borrowers = read_file(BORROWERS)
    borrowers = clean_data(borrowers[6:])
    dct_borrow = lst_to_dct2(borrowers)
    print(f"BORROWERS: {dct_borrow}")
    
    print() #spacing
    
    loans = read_file(TOTAL_LOANS)
    loans = clean_data(loans[6:])
    dct_loans = lst_to_dct2(loans)
    print(f"LOANS: {dct_loans}")

    print() #spacing
    
    # Q1.1 How many total borrowers had student loans in 2019?
 
    borrowers_2019_sum = column(dct_borrow, 3)
    print(f"The total number of borrowers in 2019 was \
          {sum(borrowers_2019_sum)}")
   
    print() #spacing
    
    # Q1.2 What is the total outstanding balance for all students 
    # as of 2021?

    loans_2021_sum = (sum(column(dct_loans, 6))) * 1000000
    print(f"The total outstanding balance for all students as of 2021 is \
          {loans_2021_sum}")
    
    print() #spacing
    
    # Q1.3 What is the average outstanding balance per student in 2016? 
    
    print(f"The average outstanding balance per student in 2016 \
          is {round(statistics.mean(column(dct_loans, 0)), 3)}")

    print() #spacing
    
    # Q2.1 What is Nevada’s average outstanding balance over all years 
    # in the dataset?
    
    print(f"Nevada's average outstanding balance over all years is\
          {(statistics.mean(dct_loans['Nevada'])) * 1000000}")
    
    print() #spacing

    # Q2.2 Which state had the greatest balance on average over all 
    # years in the dataset?
    
    greatest_state = key_from_value(dct_loans, max(dct_loans.values()))
    print(f"The state with the greatest balance on \
          average is {greatest_state}.")
          
    print() #spacing
    
    # Q2.3 What was the greatest balance on average over all
    # years in the dataset?
    
    averaged = rows_avgd(dct_loans)
    print(f"The greatest balance on average over all years in\
          the data is {max(averaged.values())*1000000}")
          
    print() #spacing
    
    # Q2.4 Which state had the lowest balance on average over all 
    # years in the dataset?
    
    lowest_state = key_from_value(dct_loans, min(dct_loans.values()))
    print(f"The state with the lowest balance on average is {lowest_state}.")

    print() #spacing
    
    # Q2.5 What was the lowest balance on average over all 
    # years in the dataset?

    averaged = rows_avgd(dct_loans)
    print(f"The lowest balance on average over all years in\
           the data is {min(averaged.values())*1000000}")
           
    print() #spacing
    
    # Q3 On average, how much did the number of borrowers in 
    # Pennsylvania change per year?
   
    avg_change = statistics.mean(chg_by_year(dct_borrow, 'Pennsylvania'))
    print(f"The average change in number of borrowers in Pennsylvania\
          per year is {avg_change}.")
          
    # Q4 A histogram showing the average outstanding balance 
    # per borrower in each state, in 2021
    
    plot_hist(dct_loans, dct_borrow)
    
    # Q5 A line chart showing how the average outstanding balance 
    # per borrower changed over time between Minnesota and Massachusetts.
    
    plot_line(dct_loans, dct_borrow)
    
    

if __name__ == "__main__":
    main()
