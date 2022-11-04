#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 3 14:38:01 2022

@author: Josh Holt"""

""" Un-comment the function call to test individual functions."""

#Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not
def day_of_week():
    day_of_week = input("What day of the week is it? Please type the whole word.")
    if day_of_week.lower() == "monday":
        print('Happy Monday!')
    else:
        print(f'Today is: {day_of_week}')

#day_of_week()

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend

def week_day():
    day_of_week = input("What day of the week is it? Please type the whole word.")
    if day_of_week.lower() == "saturday" or day_of_week.lower() == "sunday":
        print('Happy weekend!')
    else:
        print("Its a weekday, get back to work.")

#week_day()



#create variables and make up values for

    #the number of hours worked in one week
    #the hourly rate
    #how much the week's paycheck will be
    #write the python code that calculates the weekly paycheck.
        #You get paid time and a half if you work more than 40 hours

def weekly_pay():
    hours = float(input("Input hours worked this week:"))
    hr_rate = float(input("Input pay rate for this week:"))
    ot_hours = float(hours - 40)
    ot_rate = 1.5
    pay = hours * hr_rate
    if ot_hours > 0:
        pay += (ot_hours * ot_rate)
    print(f'Your paycheck will be: {pay}')
    
#weekly_pay()


"""Loop Basics

                While loop

Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.
Your output should look like this:


5
6
7
8
9
10
11
12
13
14
15
"""
def while_loop():
    i = 5
    while i <= 15:
        print(i)
        i += 1
#while_loop()
"""
#Create a while loop that will count by 2's starting with 0 and ending at 100. 
#Follow each number with a new line.
"""
def duce_while():
    i = 0
    while i <= 100:
        print(i)
        i += 2
#duce_while()

#Alter your loop to count backwards by 5's from 100 to -10.
def five_while():
    i = 100
    while i >= -10:
        print(i)
        i += -5
#five_while()
"""
Create a while loop that starts at 2, and displays the number squared on 
each line while the number is less than 1,000,000. Output should equal:


 2
 4
 16
 256
 65536
 """
def square_while():
    i = 2
    while i <= 1000000:
        print(i)
        i = i ** 2
#square_while()
"""
Write a loop that uses print to create the output shown below.


100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
"""

def five_down_while():
    i = 100
    while i > 0:
        print(i)
        i += -5
#five_down_while()
"""
                For Loops

Write some code that prompts the user for a number, then shows a multiplication 
table up through 10 for that number.

For example, if the user enters 7, your program should output:


7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
"""
def mult_tables():
    i = 1
    multiple = int(1)
    user_num = int(input("Please enter a whole numbrer: "))
    while i < 11:
        multiple = i * user_num   
        print(f' {user_num} x ', i, f' = {multiple}')
        i += 1
#mult_tables()
"""
Create a for loop that uses print to create the output shown below.


1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
def num_mid():
    i = 1
    while i < 10:
        print(i * str(i))
        i += 1
#num_mid()

""" 
                break and continue

Write a program that prompts the user for a positive integer. 
Next write a loop that prints out the numbers from the number the user entered down to 1.
"""
def user_int():
    user_num = abs(int(input("Please input a positive integer: \n")))
    while user_num >= 1:
        print(f'Your number is melting! {user_num}')
        user_num -= 1
    print("Your number has melted...")
#user_int()

"""
The input function can be used to prompt for input and use that input in your python code. 
Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
(Hints: first make sure that the value the user entered is a valid number, 
 also note that the input function returns a string, 
 so you'll need to convert this to a numeric type.)
"""
def even_num():
    i = 1
    user_num = int(input("Please enter a positive even number: \n"))
    while user_num %2 != 0 or user_num < 1:
        user_num = int(input("You did not follow directions so try again: \n"))
    
    print("Lets count together!")
    while i < user_num:
        print(i)
        i += 1     
#even_num()

"""
Prompt the user for an odd number between 1 and 50. 
Use a loop and a break statement to continue prompting the user if they enter invalid input.
    (Hint: use the isdigit method on strings to determine this). 
Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
except for the number the user entered.

Your output should look like this:


Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49
Fizzbuzz
"""
def odd_user_num():

# Int validation for user input
    while True:
        try:
            user_num = int(input("Please enter an odd number between 1 and 50. \n"))
            if (user_num < 1) or (user_num > 50) or ((user_num % 2) == 0):
                print("You did not follow directions. \n")
            else:
                break
        except ValueError:
            print("Oops, that was not a number! \n")

# Instruction validation for user number selection:
    
    print(f'Good job! Lets count odd numbers but skip {user_num}: ')
    i = 1
    
# This is the logic to count up to the number and skip selected numbers.   
    while i < 51:
        if i == user_num:
            print(f'Yikes! Skipping number: {user_num}')
            i += 1
        elif i % 2 != 0:
            print(f'Here is an odd number: {i}')
            i += 1
        elif i % 2 == 0:
            i += 1
            continue
    print('Fizzbuzz') # Not required but present in the example.
#odd_user_num()


"""
One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
Developed by Imran Ghory, the test is designed to test basic looping and conditional 
logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
Display a table of powers.
"""
def fizz_buzz():
    i = 0
    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz")
            i += 1
        elif i % 3 == 0:
            print("Fizz")
            i += 1  
        elif i % 5 == 0:
            print("Buzz")
            i += 1
        else:
            print(i)
            i += 1
#fizz_buzz()




"""
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example Output


What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125

"""
def table_num():
    num = int(input("Please enter an integer: \n"))
    i = int(1)
    print('number | squared | cubed')
    print('-------| ------- | -----')
    while i <= num:
        i_2 = i ** 2
        i_3 = i ** 3

        print(f'{i: 6} | {i_2: 8}| {i_3: 5}')
        i += 1

#table_num()


#Bonus: Research python's format string specifiers to align the table
# Check

"""
Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
"""
def grades():
    letter_grade = str()
    grade = int(input("Please provide a whole number grade from 0 - 100\n"))
    while type(grade) != int or grade < 0 or grade > 100:
        grade = int(input("You did not follow instructions, minus 3 points. Try again.\n"))
    if grade >= 88:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 67:
        letter_grade = "C"
        print("Try explaining the material to a five year old.")
    elif grade >= 60:
        letter_grade = "D"
        print("Start with the base concepts and explain them in simple terms.")
    else:
        letter_grade = "F"
        print("The only real failure is quitting.")
    print(f'You recieved a grade of {letter_grade}')


#grades()
"""

Bonus

Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
"""


def grades_bonus():
    letter_grade = str()
    grade = int(input("Please provide a whole number grade from 0 - 100\n"))
    while type(grade) != int or grade < 0 or grade > 100:
        grade = int(input("You did not follow instructions, minus 3 points. Try again.\n"))
    if grade >= 98:
        letter_grade = "A+"
    elif grade >= 90:
        letter_grade = "A"
    elif grade >= 88:
        letter_grade = "A-"
    elif grade >= 86:
        letter_grade = "B+"
    elif grade >= 82:
        letter_grade = "B"
    elif grade >= 80:
        letter_grade = "B-"   
    elif grade >= 77:
        letter_grade = "C+"
        print("Try explaining the material to a five year old.")
    elif grade >= 69:
        letter_grade = "C"
        print("Try explaining the material to a five year old.")
    elif grade >= 67:
        letter_grade = "C-"
        print("Try explaining the material to a five year old.")

# Lets be honest, at this point + and - don't matter.
    elif grade >= 60:
        letter_grade = "D"
        print("Start with the base concepts and explain them in simple terms.")
    else:
        letter_grade = "F"
        print("The only real failure is quitting.")
    print(f'You recieved a grade of {letter_grade}')
#grades_bonus()

"""
Create a list of dictionaries where each dictionary represents a book that you have read. 
Each dictionary in the list should have the keys title, author, and genre. 
Loop through the list and print out information about each book.

Prompt the user to enter a genre, then loop through your books list and print out the t
itles of all the books in that genre.
"""





























