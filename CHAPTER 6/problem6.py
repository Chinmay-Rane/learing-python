#grade calculator

g=int(input("Enter the marks: "))

if(90<g<=100):
    print("You scored an A")
elif(80<g<=90):
    print("You scored a B")
elif(70<g<=80):
    print("You scored a C")
elif(60<g<=70):
    print("You scored a D")
elif(50<g<=60):
    print("You scored a E")
elif(0<g<=50):
    print("You scored a F")
elif(g<=0):
    print("Exam diya bhi kyu tu?")