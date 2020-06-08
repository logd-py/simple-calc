#python module to find factorial of a number

#def factorial(n):
#    return 1 if (n==1 or n==0) else n*factorial(n-1);

def factorial(n):
    if n<0:
        return 0
    elif (n==0 or n==1):
        return 1
    else:
        fact=1
        while(n>1):
            fact*=n
            n-=1
        return fact

#Main driver program
num=int(input("Enter a number to find its factorial :"))

print(" The factorial of ", num ,"is", factorial(num))


