#covert degree celcius to farenheit

def convert(celcius):
    return (celcius * 9/5) + 32

celcius = int(input("Enter temp in celcius: "))
print(f"{round(convert(celcius)),2} F") #round function rounds up to specific decimal spaces here 2

