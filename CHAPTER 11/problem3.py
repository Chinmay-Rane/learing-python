class Employee:
    salary=1212
    increment=20

    @property
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment= ((salary/self.salary)-1)*100

e=Employee()
# print(e.salary,e.increment)
e.salaryAfterIncrement=1345
print(e.increment)