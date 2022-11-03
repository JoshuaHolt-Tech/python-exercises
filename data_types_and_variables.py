#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:19:47 2022

@author: joshholt
"""

#You have rented some movies for your kids: 
    #The little mermaid (for 3 days)
    #Brother Bear (for 5 days, they love it)
    #Hercules (1 day, you don't know yet if they're going to like it)
    #If price for a movie per day is 3 dollars, how much will you have to pay?
def movie_rental():
    little_mermaid = 3
    brother_bear = 5
    hercules = 1
    cost = 3

    movies = [little_mermaid, brother_bear, hercules]
    total_price = 0

    for item in movies:
        total_price += item * cost

    return print(f' Total cost is $ {total_price}')

movie_rental()    
    
    
    
    
#Suppose you're working as a contractor for 3 companies: 
    #Google - 400/hour * 6 hours
    #Amazon - 380/hour * 4 hours
    #Facebook - 350/hour * 10 hours
    
    # How much will you receive in payment for this week?
def contractor_pay():
    google_comp = 400 * 6
    amazon_comp = 380 * 4
    fb_comp = 350 * 10
    contracts = [google_comp,amazon_comp, fb_comp]
    total_comp = sum(contracts)
    return print(f' Total money earned from contracts: $ {total_comp}')
    
contractor_pay()



#A student can be enrolled to a class only:
    #if the class is not full
    #the class schedule does not conflict with her current schedule.
    
    
def enrollment_eligible():    
    enrollment_allowed = False
    class_not_full = True
    schedule_conflict = False
    
    if ((class_not_full == True) and (schedule_conflict == False)):
        enrollment_allowed = True
    return print(f' You are allowed to enroll in this class: {enrollment_allowed}')

enrollment_eligible()


#A product offer can be applied only if:
    #people buys more than 2 items
    #the offer has not expired.
    
    #Premium members do not need to buy a specific amount of products.

def valid_offer():
    quantity = 2
    offer_exp = False
    prem_mem = True
    offer_valid = False
    
    if (prem_mem == True):
        offer_valid = True
    elif (quantity > 2 ) and (offer_exp == False):
        offer_valid = True
    return print(f' Product Offer is valid: {offer_valid}')

valid_offer()

def user_pw_check():
    username = 'codeup'
    password = 'notastrongpassword'
    #Create a variable that holds a boolean value for each of the following conditions:
    
    #the password must be at least 5 characters
    #the username must be no more than 20 characters
    #the password must not be the same as the username
    #bonus neither the username or password can start or end with whitespace

    user_whitespace1 = username[0]
    user_whitespace2 = username[-1]
    pw_whitespace1 = password[0]
    pw_whitespace2 = password[-1]
    user_pw_good = False
    #This needs better logic but this is the initial idea:
    if len(password) < 4:
        print('Your password is too short. Use more than 4 char.')
        password = input('Password: ')
    if len(password) > 21:
        print('Your password is greater than 20 char, use less')
        password = input('Password: ')
    if username == password:
        print("Your username and password are the same, please change")
        username = input('Username: ')
        password = input('Password: ')
    if  user_whitespace1.isspace() == True or user_whitespace2.isspace() == True:
        print("Your username has whitespace, please remove")
        username = input(print('Please enter a new username: '))
    if  pw_whitespace1.isspace() == True or pw_whitespace2.isspace() == True:
        print("Your password has whitespace, please remove")
        password = input(print('Please enter a new password: '))
    else:
        user_pw_good = True
    
    return print(f' Your username and password are good: {user_pw_good}')


user_pw_check()









