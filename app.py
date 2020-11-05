import addition
import subtraction
import multiplication
import division

print("Please choose an operation")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division ")

userChoice = input ("Enter Choice 1 or 2 or 3 or 4  :  ")
if userChoice in ('1', '2', '3', '4'  ):
    number1 = float(input("Enter first number: "))
    number2 = float(input ("Enter second number: "))
    if (userChoice == '1'):
        print( "Result is: " addition.add(number1, number2))
    elif (userChoice == '2'):
        print("Result is: " subtraction.subtract(number1, number2))
    elif (userChoice == '3'):
        print ("Result is: " multiplication.multiply(number1, number2))
    elif (userChoice == '4'):
        print("Result is: " division.division(number1, number2))
else:
    print("Invalid user input")