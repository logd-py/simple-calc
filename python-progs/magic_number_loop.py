#Magic number program using loop
magic=7

#Ask user for a number
guess=int(input("Please guess the Magic number between 1 and 10 : "))


while magic!=guess:
    print("sorry that is not magic number")
    guess=int(input("Please retry to guess the Magic number : "))


print("Correct! yes that is the Magic number")
print("Good Bye!")

        
    
