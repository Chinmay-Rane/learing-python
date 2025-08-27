#add static attribute to great hello in problem 1

class Calculator:
    def __init__(self,n):
       self.n=n
    def square(self):
        print(f"The sqaure is {self.n*self.n}")
    def cube(self):
        print(f"The sqaure is {self.n*self.n*self.n}")
    def square_root(self):
        print(f"The sqaure is {self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Hello")
 
b=int(input("Enter a number: "))
a=Calculator(b)
a.square()
a.cube()
a.square_root()
a.greet()

