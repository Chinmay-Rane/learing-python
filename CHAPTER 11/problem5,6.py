class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        result=Vector(self.x + other.x,self.y + other.y,self.z + other.z)
        return result
    def __mul__(self,other):
        result= self.x*other.x + self.y*other.y + self.z*other.z
        return result
    def __str__(self):
        return f"({self.x}i+{self.y}j+{self.z}k)"
    

#Vector 1

vector = list(map(int, input("Enter vector 1 elements: ").split()))

# Assign each element to a variable dynamically
v1, v2, v3 = vector

vo= Vector(v1,v2,v3)

#Vector 2

vector = list(map(int, input("Enter vector 2 elements: ").split()))

# Assign each element to a variable dynamically
v4, v5, v6 = vector

vu= Vector(v4,v5,v6)

print(f"The addition of both the vectors is: {vo + vu}")
print(f"The multiplication of both the vectors is: {vo * vu}")

