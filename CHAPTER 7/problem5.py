#sum of first n natural numbers using while loop
sum=0
n=int(input("Sum of 1 to ? : "))
i=1
while(i<=n):
    sum += i #increments with the value of i
    i+=1
print(f"The sum is {sum}")