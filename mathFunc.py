def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(a,b):
    if b!=0:
        return a/b
    else:
        print('Error! Division by zero not allowed')

num1 = 10
num2 = 5

sum = add(num1, num2)
print("Sum= ", sum)

difference = subtract(num1, num2)
print("Difference= ", difference)

product = multiply(num1, num2)
print("Product= ", product)

division = multiply(num1, num2)
print("Division= ", division)
