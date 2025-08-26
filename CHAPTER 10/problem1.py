# class Programmer:
#     name="Name of the Programmer"
#     role="Role in the company"
#     exp="work experience"
# alex=Programmer()
# alex.name="Alex Saint"
# alex.role="Project Manager"
# alex.exp="4 years"
# print(alex.name,alex.role,alex.exp)
# priya=Programmer()
# priya.name="Priya Sawant"
# priya.role="Team Lead"
# priya.exp="2 years"
# print(priya.name,priya.role,priya.exp)
# neil=Programmer()
# neil.name="Neil Donald"
# neil.role="Head Developer"
# neil.exp="1 year"
# print(neil.name,neil.role,neil.exp)

# or

class Programmer:
    company="Microsoft"
    def __init__(self,name,role,exp):
        self.name=name
        self.role=role
        self.exp=exp
p=Programmer("Alex Saint","Project Manager","4 years")
print(f"Works for {p.company}\n Name: {p.name}\n Role: {p.role}\n Experience: {p.exp}")
#multiple can be added the same way

