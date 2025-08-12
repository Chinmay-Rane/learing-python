#multiplation table of a given number reversed
num=int(input("Enter the number for table: "))

for i in range(0,11):
   m=(11-i)*num
   print(f"{num}x{11-i}={m}")