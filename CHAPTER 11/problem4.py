class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    @property
    def num(self):
        return f"{self.r,self.i}"
    @num.setter
    def num(self,value):
        self.fname= value.split(+)[0]
        self.lname= value.split(+)[1]

n=Complex()
n.num=