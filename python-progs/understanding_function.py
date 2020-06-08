# this is a program to expalin function

#importing datetime module
import datetime
#importing getpass module for getting username imput
import getpass

cdt=datetime.datetime.now()
x=cdt.hour

print("Today's Date is", cdt.strftime('%d/%m/%Y'))
print("current time is ",cdt.strftime('%H:%M:%S'))
print("")
#print(cdt.strftime('%c'))
#b = [0,4,8,12,16,20,24]
#l = ['Late Night', 'Early Morning','Morning','Noon','Eve','Night']

def f(x):
    if (x > 5) and (x <= 12 ):
        return 'Morning!!'
    elif (x > 12) and (x <= 16):
        return'Noon!!'
    elif (x > 16) and (x <= 20) :
        return 'Evening!!'
    else:
        return'Night!!'

def greet():
    print("Hey",getpass.getuser(),"Good",f(x))
    
print("Today is",cdt.strftime('%A'))
print("")
greet()


