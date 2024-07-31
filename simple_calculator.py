#Desiging a simple calculator
number_1 = int(input("Enter the value1:"))
number_2 = int(input("Enter the value_2:"))
operator = input("Enter the operator:")
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def exponential(a,b):
    return a**b
def floor_division(a,b):
    return a//b

if operator=="+":
    add=addition(number_1,number_2)
    print("The sum {0} and {1} numbers is:".format(number_1, number_2), add)
elif operator=="-":
    sub = subtraction(number_1, number_2)
    print("The subtraction {0} and {1} numbers is:".format(number_1, number_2), sub)
elif operator=="*":
    mul=multiplication(number_1,number_2)
    print("The multiplication {0} and {1} numbers is:".format(number_1,number_2),mul)
elif operator=="/":
    div=division(number_1,number_2)
    print("The division {0} and {1} numbers is:".format(number_1,number_2),div)
elif operator=="**":
    exp=exponential(number_1,number_2)
    print("The exponential {0} and {1} numbers is:".format(number_1,number_2),exp)
else:
    floordiv=floor_division(number_1,number_2)
    print("The floordivision {0} and {1} numbers is:".format(number_1,number_2),floordiv)



