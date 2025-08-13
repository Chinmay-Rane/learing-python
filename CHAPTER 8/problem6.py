#covert inches to centimeters

def convert(inches):
    return (inches *2.54)

inches = int(input("Enter length in inches: "))
print(f"{convert(inches)} cm") #round function rounds up to specific decimal spaces here 2
