#Program to roll the Digital dice

#importing random to provide random output
import random
import time

min = 1
max = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print("Rolling the Dice..")
    print("The Values are...")
    time.sleep(2)
    print(random.randint(min, max),"&",random.randint(min, max))
    #print(random.randint(min, max))

    roll_again = input("Do you want to Roll again?")
