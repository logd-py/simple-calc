#Python program for palindrome.

x=input("Enter the string to be checked for Palindrome: ")
y=x[::-1]

if (x==y):
    print("The entered string",x,"is a Palindrome.")
else:
    print("The entered string",x,"is not a palindrome.")

          
