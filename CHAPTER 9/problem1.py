with open("CHAPTER 9/poems.txt") as f:
    c= f.read()
if("twinkle"in c):
    print("There is a twinkle")
else:
    print("No twinkle")