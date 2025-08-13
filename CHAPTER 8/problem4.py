#recursive function to print sum of n natural numbers

def sum(n):
    if(n==1):  #base is added so that the function doesnt go infinitely in negatives
        return 1
    return sum(n-1)+n
    
n=int(input("Enter the number: "))

print(f"The sum is {sum(n)}")