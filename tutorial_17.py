import numpy as np

num = []
multipliers = [5, 4, 3, 2]

boundary = 4

def mod_11():
    for i in range(0,boundary):
        given_nums = int(input("Mr White, give me a number! "))
        num.append(given_nums)
    
    multiplied = list(np.multiply(num, multipliers))
    #used numpy to multiply two lists together, so useful!
    
    final = sum(multiplied)
    #I never knew there was a sum function
    
    mod = final%11
    
    check_digit = 11 - mod 
    #Finally calcultating the check digit
    
    print ("Yo! The check digit is", check_digit, "Mr White!")
    
mod_11()
