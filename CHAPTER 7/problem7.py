#star pattern 1

n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")  #end by default doesnt add line breaks
    print("\n")