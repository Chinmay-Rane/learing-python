def table():
    n=int(input("Enter the number: "))

    tab=[n*i for i in range (1,11)]
    
    return tab,n

if __name__=="__main__":
    o,n=table()
    print(f"The Multiplication Table of {n}")
    for i in range (0,10):
            
        print(o[i])
