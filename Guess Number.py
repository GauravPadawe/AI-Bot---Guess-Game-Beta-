import random
import sys

def guess(a):
    x = [1,2,3,4,5,6,7,8,9]
    while True:
        cpu = random.choice(x)
        if a < cpu:
            return "Less"
        elif a > cpu:
            return "Greater"
        elif a == cpu:
            return "Equal"
            sys.exit()
        
def again():
    y = [1,2,3,4,5,6,7,8,9]
    while True:
        try:
            user = int(input("What's your Choice ?"))
            if user not in y:
                return "Out of context, just choose between 1 to 9"
            else:
                print (guess(user))
        except:
            return "Invalid Input, try again"
            continue
    
print (guess(9))