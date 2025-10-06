from problem3 import table
o,n=table()

with open("Tables.txt","w") as f:
    f.write(f"The Table of {n}:{o}"+"\n")

print(f"The table of {n} is stored in 'Tables.txt")