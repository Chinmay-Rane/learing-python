#what will be the length of this string??

s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s),s) #returns 2 as 20==20.0 values are same datatype doesnt matter
print(3==len(s)) #returns False if 3 true if 2