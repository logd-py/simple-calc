#BMI Calculator

#Ask user for input

height=float(input("Please provide height in Meters: "))
weight=float(input("Please provide height in Kilograms: "))

#calculating the BMI:

BMI=weight/(height**2)

print(" Your BMI is ",round(BMI,2))

if BMI<18:
	print("You are underweight per your BMI, Need to improve")
else:
	if BMI>25:
		print("Sorry, You are overweight per your BMI")
	else:
		print("Congrats, You are healthy weight per your BMI")
