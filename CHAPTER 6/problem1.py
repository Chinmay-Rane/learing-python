#greatest of 4

a=int(input("Enter number A: "))
b=int(input("Enter number B: "))
c=int(input("Enter number C: "))
d=int(input("Enter number D: "))

if(a>b and a>c and a>d):
    print("A is greater:",a)

if(b>a and b>c and b>d):
    print("B is greater:",b)

if(c>b and c>a and c>d):
    print("C is greater:",c)

if(d>b and d>c and d>a):
    print("D is greater:",d)

if(a==b==c==d):
    print("All equal")

