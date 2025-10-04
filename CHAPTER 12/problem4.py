a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

try:
    print(f"The Division is {a/b}")
except ZeroDivisionError as e:
    e="The Division goes to Infinity"
    print(e)