def add(num1, num2):
    return num1+num2

def minus(num1, num2):
    return num1-num2

def times(num1, num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def calculator(num1, num2, operator):
    print(operator)
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return minus(num1,num2)
    elif operator == "*":
       return  times(num1,num2)
    elif operator == "/":
        return divide(num1,num2)

n1 = int(input("Enter a number\n"))
operator = input("+\n-\n/\n*\n\n")
n2 = int(input("Enter a number\n"))

calculate = calculator(n1, n2, operator)

print(calculate)