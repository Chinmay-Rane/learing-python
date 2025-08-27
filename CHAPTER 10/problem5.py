# train reservation
from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"The train with no:{self.trainNo} is booked from:{fro} to:{to}")

    def getStatus(self,fro,to):
        print(f"The train with train no:{self.trainNo} has departed from:{fro} to:{to} is {randint(0,1500)}")

    def getFare(self,fro,to):
        print(f"The fare for train no:{self.trainNo} from:{fro} to:{to} is {randint(0,1500)}")

t=Train(12321213)
t.book("Pune",'Kankavli')