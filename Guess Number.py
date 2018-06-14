import random
import sys

def guess(a):                             # def guess function
    x = [1,2,3,4,5,6,7,8,9]
    while True:                           # while loop to keep running again
        cpu = random.choice(x)            # cpu will choose random number from list
        if a < cpu:                       # if value of a < cpu
            return "Less"
        elif a > cpu:                     # else if a > cpu
            return "Greater"
        elif a == cpu:                    # else if a == cpu
            return "Equal"
            sys.exit()
        
def again():                                # Defining another function
    y = [1,2,3,4,5,6,7,8,9]
    while True:                             # while
        try:                                                          # try if user input integer or string
            user = int(input("What's your Choice ?"))
            if user not in y:                                         # if user value is not in list Y
                return "Out of context, just choose between 1 to 9"   # print out of context
            else:                                                     # else run functio guess with intialised value
                print (guess(user))
        except:                                                       # if string then return Invalid Input
            return "Invalid Input, try again"
    
print (guess(9))

# To be developed ....
# CODED BY - GAURAV PADAWE
