#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#if __name__ == '__main__':
   
"""
Created on Fri Nov  4 09:07:28 2022

@author: joshholt
"""
"""
Define a function named is_two. 
-It should accept one input
-Return True if the passed input is:
    -either the number or string 2
-Otherwise False.
"""
def is_two(item):
    """
    This function accepts int or str 2 and returns True, otherwise False.
    """
    if item == 2 or item == '2':
        return True
    else:
        return False
#print(is_two('3'))

"""
Define a function named is_vowel. 
-It should return True if the passed string is a vowel.
-Otherwie False.
"""
def is_vowel(item):
    """
    Returns True if a vowel is passed into the function.
    """
    lst = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if type(item) != str:
        return False
    
    for letter in item:
        lst.append(letter)
    for i in lst:
        if i in vowels:
            return True
    return False

#print(is_vowel('o'))

"""
Define a function named is_consonant.
-It should return True if:
    The passed string is a consonant
    Otherwise False. 
    Use your is_vowel function to accomplish this.

"""
def is_consonant(item1):
    """
    
    """
    if isinstance(item1, str) == False:
        return False
    elif item1.isalpha() == False:
        return False
    elif is_vowel(item1) == True:
        return False
    else:
        return True

#print(is_consonant('d'))

"""
Define a function that accepts a string that is a word.
The function should capitalize the first letter of the word if the word starts with a consonant.
"""

def caps_first_word(item):
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    if item[0].isalpha() != True:
        if item[0] not in vowels:
            return print(item.capitalize())
        
    print(item)
#caps_first_word('dusk')

"""
Define a function named calculate_tip. 
It should accept: 
    tip percentage (a number between 0 and 1) 
    the bill total
return the amount to tip.
"""

def calculate_tip(percent_tip, bill_total):
    while True:
        if 0.0 < percent_tip < 1.0 and type(percent_tip) == float:
            break
        else:
            percent_tip = float(input("Please tip using percent value between 0.0 and 1.0\n"))

    return print('You should tip: $',bill_total * (percent_tip))
    
    
#calculate_tip(percent_tip= 5, bill_total= 15)
"""
Define a function named apply_discount.
It should accept a original price, and 
a discount percentage, and 
return the price after the discount is applied.
"""
def apply_discount(origional_price, discount_precentage):
    return origional_price * (1 - discount_precentage)


#apply_discount()
"""
Define a function named handle_commas. 
It should accept a string that is a number that contains commas in it as input, and 
return a number as output.
"""
def handle_commas(input_str):
    num_list= ['0','1','2','3','4','5','6','7','8','9']
    return_str = ""
    for item in input_str:
        if item != ',' and item in num_list:
            return_str += item
    return print(return_str)

#handle_commas('34664,34543')

"""
Define a function named get_letter_grade. 
It should accept a number and 
return the letter grade associated with that number (A-F).
"""
def get_letter_grade(input_num):
    input_num = int(input_num)
    if input_num >=90:
        return print("A")
    elif input_num >=80:
        return print("B")
    elif input_num >=70:
        return print("C")    
    elif input_num >=60:
        return print("D")    
    else:
        return print("F" )   
    


#get_letter_grade(65)

"""
Define a function named remove_vowels that 
accepts a string and returns a string with all the vowels removed.
"""
def remove_vowels(input_str):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return_str = ""
    for item in input_str:
        if item in vowels:
            continue
        else:
            return_str += item
    return print(return_str)

#remove_vowels("Sophisticated")

"""
Define a function named normalize_name. 
It should accept a string and 
return a valid python identifier, that is:
-anything that is not a valid python identifier should be removed
-leading and trailing whitespace should be removed
-everything should be lowercase
-spaces should be replaced with underscores
-for example:
    Name will become name
    First Name will become first_name
    % Completed will become completed
"""
def normalize_name(input_str):
    input_str = input_str.lower().strip()
    return_str = ""
    for item in input_str:
        if item == " ":
            return_str += '_'
        elif item.isalnum() == False:
            continue
        else:
            return_str += item
    return return_str

#print(normalize_name('@gimD %fa$Ct'))

"""
Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
"""
def cumulative_sum(input_list):
    list_sum = 0
    for item in input_list:
        list_sum += item
    input_list.append(list_sum)
    return print(input_list)

test_list = [3,5,6,7,5,9]
#cumulative_sum(test_list)

"""        *** Bonus ***
Create a function named twelveto24. 
It should accept a string in the format 10:45am or 4:30pm and 
return a string that is the representation of the time in a 24-hour format. 
"""
def twelveto24(input_str):

    # Seperates hours from minutes
    hour_split = input_str.split(':')
    # Changers hours from str to int
    hours = int(hour_split[0])
    # Snags the 'am' or 'pm' to be evaluated later.
    am_pm = hour_split[1][2:]
    # Identifys 'pm' and adds 12 hours.
    if am_pm.lower() == 'pm':
        hours += 12
    # Changes hours to str and adds the minutes back in.
    output_str= str(hours) + input_str[-4:-2]
    return print(output_str)
    

#twelveto24('4:45pm')
"""
Bonus write a function that does the opposite.
"""
def twentyfourto12(input_str):
    hours = int(input_str[:2])
    output_str = ""
    if hours > 12:
        output_str = str(hours-12) + ':'+ input_str[-2:] + 'pm'
    else:
        output_str = str(hours) +':'+ input_str[-2:] + 'am'
    return print(output_str)
    
#twentyfourto12('1932')
"""
Create a function named col_index. 
It should accept a spreadsheet column name, and return the index number of the column.
    col_index('A') returns 1
    col_index('B') returns 2
    col_index('AA') returns 27
"""
# Brute force is having a dictionary/list to return the index. 
# Be lazy.
def col_index():
    pass



























