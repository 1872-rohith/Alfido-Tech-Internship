#Task 1 - A Simple Calculator using Python
operator = input("Enter an Operator(+ - * /):")
number1 = float(input("Enter The 1st Number:"))
number2 = float(input("Enter The 2nd Number:"))
 
if operator == "+":
    result = number1 + number2
    print(round(result))
elif operator == "-":
    result = number1 - number2
    print(round(result))
elif operator == "*":
    result = number1 * number2
    print(round(result))
elif operator == "/":
    result = number1 / number2
    print(round(result))
else:
    print(f"{operator} is not valid Operator")
