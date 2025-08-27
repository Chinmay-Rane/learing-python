class example:
    a=4
obj=example()
print(obj.a)
obj.a=0
print(obj.a)
print(example.a)

#this doesnt change the class attribute(only for instance obj)
#but uses instance attribute to update it
