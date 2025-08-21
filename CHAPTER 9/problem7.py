#find which line has python in it



with open("CHAPTER 9/log.txt") as f:
    lines=f.readlines()
lineno=1
for line in lines:
    if "python" in line:
        print(f"python in logs at line number {lineno}")
        break
    lineno+= 1
else:
    print("python not in logs")