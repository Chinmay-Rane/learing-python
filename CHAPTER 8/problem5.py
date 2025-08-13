#star pattern in function

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    return pattern(n-1)

n=int(input("Enter the number: "))

print(pattern(n))