#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:59:25 2022

@author: joshholt
"""
"""
Import and test 3 of the functions from your functions exercise file. 
Import each function in a different way:
"""
from functions_exercises import cumulative_sum #No .py on the end of the file.
some_list = [2,3,4,5,9,2,5,5,3,2,2,5,5]
cumulative_sum(some_list)

from functions_exercises import normalize_name

normalize_name('John Doe')

from functions_exercises import remove_vowels

remove_vowels('John Doe')

"""
Run an interactive python session and import the module. 
"""
# Done

"""
    Call the is_vowel function using the dot syntax.
"""
import functions_exercises
print(functions_exercises.is_vowel('o'))
"""
    Create a file named import_exericses.py. 
    Within this file, use from to import the calculate_tip function directly. 
    Call this function with values you choose and print the result.
"""
# import done above:
#print(functions_exercises.calculate_tip(.3, 100))
"""
    Create a jupyter notebook named import_exercises.ipynb. 
    Use from to import the get_letter_grade function and give it an alias. 
    Test this function in your notebook.
"""
# Done

"""
Make sure your code that tests the function imports is run from the same directory 
that your functions exercise file is in.
"""
# Done
"""
Read about and use the itertools module from the python standard library
to help you solve the following problems:

    How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
    How many different combinations are there of 2 letters from "abcd"?
    How many different permutations are there of 2 letters from "abcd"?
"""
import itertools

print(list(itertools.product('abc', '123')))
print(len(list(itertools.combinations("abcd", 2))))
print(len(list(itertools.permutations('abcd', 2))))

"""
Save this file as profiles.json inside of your exercises directory 
(right click -> save file as...).

Use the load function from the json module to open this file.
"""

import json


json_file = json.load(open('profiles.json'))
#print(json_file[2].keys())

count = 0
total_due = float()
min_due = float(400000) #This can't be set to zero or it won't find the lowest.
max_due = float()



for item in json_file:
    if item.get('isActive') == False:
        amount_due = item.get('balance').replace('$','').replace(',', '')
        amount_due = float(amount_due)
        if amount_due < min_due:
            min_due = amount_due
            min_user = item.get('name')

        if amount_due > max_due:
            max_due = amount_due
            max_user = item.get('name')

        
        total_due += amount_due
        count += 1

avg_due = total_due/count        

print("Everyone owes: $", round(total_due, 2))
print("The average due is: $", round(avg_due, 2))
print("The max balance due is: $", round(max_due, 2), ' from', max_user)
print("The min balance due is: $", round(min_due, 2), ' from', min_user)


"""
Your code should produce a list of dictionaries. 
Using this data, write some code that calculates and outputs the following information:
"""
    #Total number of users = 19
    #Number of active users = 9
    #Number of inactive users = 10


for item in json_file:
    if item.get('isActive') == True:
        count += 1
    
    
    
    
    #Grand total of balances for all users = $ 29,415.28
    #Average balance per user = $2,941.53
    #User with the lowest balance Avery Flynn - $1214.10
    #User with the highest balance Fay Hammond - $3919.64

# This code was used to find the above information.
count = 0
total_due = float()
min_due = float(400000)
max_due = float()


for item in json_file:
    if item.get('isActive') == False:
        print(item.get('name'), 'owes: ', item.get('balance'))
        amount_due = float(amount_due)
        
        if amount_due < min_due:
            min_due = amount_due
            min_user = item.get('name')

        if amount_due > max_due:
            max_due = amount_due
            max_user = item.get('name')

        
        total_due += amount_due
        count += 1

avg_due = total_due/count        

print("Everyone owes: $", round(total_due, 2))
print("The average due is: $", round(avg_due, 2))
print("The max balance due is: $", round(max_due, 2), ' from', max_user)
print("The min balance due is: $", round(min_due, 2), ' from', min_user)



    #Most common favorite fruit: Strawberry - 9
    #Least most common favorite fruit: Apple - 4


fruit_list = []
for item in json_file:
    fruit_list.append(item.get('favoriteFruit'))
print("Strawberry: ", fruit_list.count('strawberry'))
print("Banana: ", fruit_list.count('banana'))
print("Apple: ", fruit_list.count('apple'))


    #Total number of unread messages for all users - 210 unread messages.


total_unread = 0
for item in json_file:
    greet_list = item.get("greeting").split()
    for thing in greet_list:
        if thing.isnumeric() == True:
            total_unread += int(thing)

print(total_unread)


