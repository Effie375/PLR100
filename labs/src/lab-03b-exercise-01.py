# Program to divide two numbers and
# multiply the result with a new number

# Read two numbers
number1 = input("First number: ")
number2 = input("Second number: ")
# Convert numbers to floats
number1 = float(number1)
number2 = float(number2)
# Divide two numbers
division = number1 / number2

# Display the division
# will print value in float
print("The division of ", number1, " and ", number2, " is :", division)
# Read third number
number3 = input('\nThird number: ')
# Convert number to integer
number3 = int(number3)
# Multiply two numbers
result = int(number3 * division)
# Display the multiplication
print("The multiplication of", number3, "and", division, "is", result)
#print("The multiplication of %2d and %5.2f is %.2d" % (number3, division, result))
